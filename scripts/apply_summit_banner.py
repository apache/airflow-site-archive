#!/usr/bin/env python3
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Apply (or remove) the temporary Airflow Summit banner in the archived docs.

The published website (apache/airflow-site) adds a temporary Summit banner to the
``sphinx_airflow_theme`` header (``header.html``): an ``<a>`` element placed right
before ``<nav class="js-navbar-scroll navbar">`` plus a ``style="top: 40px;"`` shift
on the nav so the page content drops below the banner.

The docs in this archive are already-generated static HTML built with that theme, so
we cannot rebuild them - instead this script rewrites the generated HTML directly to
match what a freshly-built page would contain.

Scope: the *latest version* of every sub-project under ``docs-archive``:

* versioned sub-projects (have a ``stable/`` directory) -> only ``stable/`` is touched
  (``stable`` is byte-identical to the highest numbered version);
* non-versioned sub-projects (no ``stable/`` - currently ``apache-airflow-providers``
  and ``docker-stack``) -> the whole sub-project directory is touched.

The operation is idempotent: any pre-existing Summit banner (e.g. a previous year's)
is stripped before the current one is inserted, so re-running - or running over docs
that were built while an older banner was live - converges to a single current banner.
Use ``--remove`` to strip the banner once the Summit is over.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# --- Banner content (keep in sync with apache/airflow-site sphinx_airflow_theme/header.html) ---
BANNER_URL = "https://airflowsummit.org"
BANNER_TEXT = (
    "Airflow Summit 2026 is coming August 31 - September 2 in Austin, TX. "
    "Register now to secure your spot!"
)
BANNER_CLASS = "d-block fixed-top px-3 py-2 bg-success text-center text-bold text-white"
NAV_STYLE = "top: 40px;"

# The plain (banner-less) nav line as emitted by the theme.
NAV_MARKER = '<nav class="js-navbar-scroll navbar"'

# Matches the nav opening tag, capturing its indentation and (optional) existing attrs.
NAV_RE = re.compile(
    r'(?P<indent>[ \t]*)<nav class="js-navbar-scroll navbar"(?P<attrs>[^>]*)>'
)

# Matches an existing Summit banner anchor (any year) - identified by the airflowsummit
# URL together with the ``fixed-top`` banner class, so we never touch in-content links.
BANNER_RE = re.compile(
    r'[ \t]*<a href="https://airflowsummit\.org"[^>]*\bfixed-top\b[^>]*>.*?</a>\n',
    re.DOTALL,
)


def _strip_existing_banner(content: str) -> str:
    """Remove any existing Summit banner anchor and reset the nav tag to its plain form."""
    content = BANNER_RE.sub("", content)
    content = NAV_RE.sub(lambda m: f'{m.group("indent")}{NAV_MARKER}>', content)
    return content


def transform(content: str, *, remove: bool) -> tuple[str, bool]:
    """Return (new_content, changed) for a single HTML document."""
    if NAV_MARKER not in content:
        return content, False

    stripped = _strip_existing_banner(content)

    if remove:
        return stripped, stripped != content

    def _insert(match: re.Match) -> str:
        indent = match.group("indent")
        return (
            f'{indent}<a href="{BANNER_URL}" target="_blank" class="{BANNER_CLASS}">\n'
            f"{indent}    {BANNER_TEXT}\n"
            f"{indent}</a>\n"
            f'{indent}{NAV_MARKER} style="{NAV_STYLE}">'
        )

    new_content = NAV_RE.sub(_insert, stripped, count=1)
    return new_content, new_content != content


def iter_target_dirs(docs_path: Path):
    """Yield the directory to process for the latest version of each sub-project."""
    for sub in sorted(p for p in docs_path.iterdir() if p.is_dir()):
        stable = sub / "stable"
        if stable.is_dir():
            yield sub.name, stable  # versioned -> latest == stable
        else:
            yield sub.name, sub  # non-versioned -> the whole sub-project


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--docs-path",
        default="docs-archive",
        type=Path,
        help="Path to the docs archive root (default: docs-archive)",
    )
    parser.add_argument(
        "--remove",
        action="store_true",
        help="Remove the Summit banner instead of adding it",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change without writing any files",
    )
    args = parser.parse_args()

    docs_path: Path = args.docs_path
    if not docs_path.is_dir():
        parser.error(f"docs path not found: {docs_path}")

    verb = "Removing" if args.remove else "Applying"
    mode = " (dry-run)" if args.dry_run else ""
    print(f"{verb} Summit banner across latest docs under {docs_path}{mode}\n")

    total_changed = 0
    total_seen = 0
    for name, target in iter_target_dirs(docs_path):
        changed = 0
        seen = 0
        for html in target.rglob("*.html"):
            seen += 1
            original = html.read_text(encoding="utf-8")
            new_content, did_change = transform(original, remove=args.remove)
            if did_change:
                changed += 1
                if not args.dry_run:
                    html.write_text(new_content, encoding="utf-8")
        total_changed += changed
        total_seen += seen
        rel = target.relative_to(docs_path)
        if changed:
            print(f"  {name:<55} {rel}/  -> {changed}/{seen} files")
    print(f"\nDone. {total_changed} file(s) changed across {total_seen} HTML file(s) scanned.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
