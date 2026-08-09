#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Update SHA-pinned GitHub Actions and pre-commit hooks to their latest versions.

This replaces Dependabot for the `github-actions` and `pre-commit` ecosystems.
Dependabot clones the whole repository before its file fetcher runs, and this
repository is far too big for that (800k+ files, 47+ GB), so every Dependabot
job times out and updates never land. This script only ever reads
`.github/workflows`, `.github/actions` and `.pre-commit-config.yaml`, so it runs
from a sparse checkout in seconds.

Only pinned references are touched, and the pinning style is preserved:

    uses: actions/checkout@<sha>  # v7.0.1     -> newest release tag
    uses: apache/some-action@<sha>  # main     -> newest commit on that branch
    rev: <sha>  # frozen: v1.29.0              -> newest release tag

A cooldown window (7 days by default, matching the Dependabot config this
replaces) keeps us off releases that are still hot.

Set GITHUB_TOKEN (or GH_TOKEN) to avoid the unauthenticated API rate limit.
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import UTC, datetime, timedelta
from pathlib import Path
from time import sleep

API_ROOT = "https://api.github.com"
API_ATTEMPTS = 3
# Enough history to find the newest release outside the cooldown window without
# pulling megabytes of release notes for repositories that publish a lot.
API_PAGE_SIZE = 30

# `uses: owner/repo[/sub/path]@<40-hex sha>  # <tag-or-branch>`
USES_RE = re.compile(
    r"(?P<prefix>uses:\s+)"
    r"(?P<repo>[A-Za-z0-9._-]+/[A-Za-z0-9._-]+)"
    r"(?P<subpath>(?:/[^@\s]+)?)"
    r"@(?P<sha>[0-9a-f]{40})"
    r"(?P<gap>\s+#\s+)"
    r"(?P<comment>\S+)"
)
# `- repo: https://github.com/owner/repo`
PRE_COMMIT_REPO_RE = re.compile(r"^\s*-\s+repo:\s+https://github\.com/(?P<repo>[^\s/]+/[^\s/]+?)(?:\.git)?\s*$")
# `rev: <sha>  # frozen: v1.29.0`
PRE_COMMIT_REV_RE = re.compile(r"^(?P<prefix>\s*rev:\s+)(?P<rev>\S+)(?P<gap>\s+#\s+frozen:\s+)(?P<tag>\S+)\s*$")
# Strict release versions only - no prereleases, no moving major/minor tags.
VERSION_RE = re.compile(r"^v?(?P<version>\d+(?:\.\d+)*)$")


class GitHubError(RuntimeError):
    """Raised when the GitHub API cannot answer a question we need answered."""


def api(path: str, **params: str | int) -> list | dict | None:
    """Call the GitHub REST API, returning None for a 404.

    Transient failures (dropped connections, truncated responses, 5xx) are
    retried - a single flaky read should not fail the whole update run.
    """
    url = f"{API_ROOT}/{path}"
    if params:
        url += "?" + "&".join(f"{key}={value}" for key, value in params.items())
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    for attempt in range(1, API_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.loads(response.read())
        except urllib.error.HTTPError as error:
            if error.code == 404:
                return None
            if error.code < 500 or attempt == API_ATTEMPTS:
                raise GitHubError(f"GET {url} failed: {error.code} {error.reason}") from error
        except (urllib.error.URLError, http.client.HTTPException, TimeoutError) as error:
            if attempt == API_ATTEMPTS:
                raise GitHubError(f"GET {url} failed: {error}") from error
        sleep(attempt)
    return None


def parse_version(tag: str) -> tuple[int, ...] | None:
    """Turn `v1.29.0` into `(1, 29, 0)`, or return None if it is not a release version."""
    match = VERSION_RE.match(tag)
    if not match:
        return None
    return tuple(int(part) for part in match.group("version").split("."))


def released_at(entry: dict) -> datetime:
    return datetime.fromisoformat(entry["published_at"])


def latest_release_tag(repo: str, cutoff: datetime) -> str | None:
    """Newest release tag of `repo` that was published before `cutoff`.

    Releases are preferred over tags because they carry a publication date and
    exclude drafts, prereleases and moving major tags such as `v7`. Repositories
    that do not publish releases fall back to tags, dated by their commit.
    """
    releases = api(f"repos/{repo}/releases", per_page=API_PAGE_SIZE) or []
    candidates = [
        (version, release["tag_name"])
        for release in releases
        if not release["draft"] and not release["prerelease"] and released_at(release) <= cutoff
        for version in [parse_version(release["tag_name"])]
        if version
    ]
    if candidates:
        return max(candidates)[1]

    tags = api(f"repos/{repo}/tags", per_page=API_PAGE_SIZE) or []
    dated = sorted(
        ((version, tag["name"], tag["commit"]["sha"]) for tag in tags for version in [parse_version(tag["name"])] if version),
        reverse=True,
    )
    for _, name, sha in dated:
        commit = api(f"repos/{repo}/commits/{sha}")
        if commit and datetime.fromisoformat(commit["commit"]["committer"]["date"]) <= cutoff:
            return name
    return None


def tag_sha(repo: str, tag: str) -> str:
    """Commit SHA a tag points at, dereferencing annotated tags."""
    reference = api(f"repos/{repo}/git/ref/tags/{tag}")
    if not reference:
        raise GitHubError(f"tag {tag} not found in {repo}")
    target = reference["object"]
    if target["type"] == "tag":
        target = api(f"repos/{repo}/git/tags/{target['sha']}")["object"]
    return target["sha"]


def latest_branch_sha(repo: str, branch: str, cutoff: datetime) -> str | None:
    """Newest commit on `branch` that is older than `cutoff`."""
    commits = api(f"repos/{repo}/commits", sha=branch, until=cutoff.strftime("%Y-%m-%dT%H:%M:%SZ"), per_page=1)
    return commits[0]["sha"] if commits else None


class Updater:
    """Resolves and applies pin updates, collecting a report as it goes."""

    def __init__(self, cutoff: datetime, dry_run: bool = False) -> None:
        self.cutoff = cutoff
        self.dry_run = dry_run
        self.updates: list[tuple[str, str, str]] = []
        self.resolved: dict[tuple[str, str], tuple[str, str] | None] = {}

    def write(self, path: Path, content: str) -> None:
        if not self.dry_run:
            path.write_text(content)

    def resolve(self, repo: str, current_tag: str, current_sha: str) -> tuple[str, str] | None:
        """Return the (tag, sha) this pin should move to, or None to leave it alone."""
        key = (repo, current_tag)
        if key not in self.resolved:
            self.resolved[key] = self._resolve(repo, current_tag, current_sha)
        target = self.resolved[key]
        return target if target and target[1] != current_sha else None

    def _resolve(self, repo: str, current_tag: str, current_sha: str) -> tuple[str, str] | None:
        current_version = parse_version(current_tag)
        if current_version is None:
            # A branch pin such as `# main` - move it along the branch instead.
            sha = latest_branch_sha(repo, current_tag, self.cutoff)
            return (current_tag, sha) if sha else None
        tag = latest_release_tag(repo, self.cutoff)
        if tag is None:
            print(f"  ! {repo}: no release older than the cooldown window, left at {current_tag}")
            return None
        if parse_version(tag) < current_version:
            print(f"  ! {repo}: newest eligible release {tag} is older than the pinned {current_tag}, left alone")
            return None
        return tag, tag_sha(repo, tag)

    def record(self, name: str, before_tag: str, before_sha: str, after_tag: str, after_sha: str) -> None:
        if before_tag == after_tag:
            # A branch pin, or a tag that was moved to a different commit - the
            # tag alone would read as a no-op, so show what actually changed.
            before, after = f"{before_tag} ({before_sha[:7]})", f"{after_tag} ({after_sha[:7]})"
        else:
            before, after = before_tag, after_tag
        # The same action is typically pinned in several places - report it once.
        if (name, before, after) in self.updates:
            return
        self.updates.append((name, before, after))
        print(f"  * {name}: {before} -> {after}")

    def update_workflows(self, paths: list[Path]) -> None:
        for path in sorted(paths):
            content = original = path.read_text()
            for match in list(USES_RE.finditer(original)):
                repo, current_tag, current_sha = match["repo"], match["comment"], match["sha"]
                target = self.resolve(repo, current_tag, current_sha)
                if not target:
                    continue
                tag, sha = target
                replacement = (
                    f"{match['prefix']}{repo}{match['subpath']}@{sha}{match['gap']}{tag}"
                )
                content = content.replace(match.group(0), replacement)
                self.record(f"{repo}{match['subpath']}", current_tag, current_sha, tag, sha)
            if content != original:
                self.write(path, content)

    def update_pre_commit(self, path: Path) -> None:
        if not path.exists():
            return
        lines = path.read_text().splitlines(keepends=True)
        repo: str | None = None
        for index, line in enumerate(lines):
            repo_match = PRE_COMMIT_REPO_RE.match(line)
            if repo_match:
                repo = repo_match["repo"]
                continue
            rev_match = PRE_COMMIT_REV_RE.match(line)
            if not (repo and rev_match):
                continue
            target = self.resolve(repo, rev_match["tag"], rev_match["rev"])
            if not target:
                continue
            tag, sha = target
            lines[index] = f"{rev_match['prefix']}{sha}{rev_match['gap']}{tag}\n"
            self.record(repo, rev_match["tag"], rev_match["rev"], tag, sha)
        self.write(path, "".join(lines))

    def report(self) -> str:
        if not self.updates:
            return "No updates available outside the cooldown window.\n"
        widths = [max(len(row[column]) for row in self.updates) for column in range(3)]
        header = f"| {'Dependency':<{widths[0]}} | {'From':<{widths[1]}} | {'To':<{widths[2]}} |\n"
        divider = f"|{'-' * (widths[0] + 2)}|{'-' * (widths[1] + 2)}|{'-' * (widths[2] + 2)}|\n"
        rows = "".join(
            f"| {name:<{widths[0]}} | {before:<{widths[1]}} | {after:<{widths[2]}} |\n"
            for name, before, after in self.updates
        )
        return header + divider + rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cooldown-days", type=int, default=7, help="ignore releases newer than this many days")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).parent.parent, help="repository root")
    parser.add_argument("--summary-file", type=Path, help="write the markdown summary table here")
    parser.add_argument("--dry-run", action="store_true", help="report what would change without writing files")
    args = parser.parse_args()

    now = datetime.now(UTC)
    cutoff = now - timedelta(days=args.cooldown_days)
    print(f"Updating pins to the newest versions released before {cutoff:%Y-%m-%d %H:%M} UTC "
          f"({args.cooldown_days}-day cooldown)")

    workflows = sorted(
        {
            *(args.repo_root / ".github" / "workflows").glob("*.y*ml"),
            *(args.repo_root / ".github" / "actions").rglob("*.y*ml"),
        }
    )
    pre_commit_config = args.repo_root / ".pre-commit-config.yaml"

    updater = Updater(cutoff, dry_run=args.dry_run)
    try:
        print("GitHub Actions:")
        updater.update_workflows(workflows)
        print("Pre-commit hooks:")
        updater.update_pre_commit(pre_commit_config)
    except GitHubError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    summary = updater.report()
    print(summary, end="")
    if args.summary_file:
        args.summary_file.write_text(summary)
    if step_summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        Path(step_summary).write_text(f"### Pinned dependency updates\n\n{summary}")
    if github_output := os.environ.get("GITHUB_OUTPUT"):
        with Path(github_output).open("a") as output:
            output.write(f"updated={'true' if updater.updates else 'false'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
