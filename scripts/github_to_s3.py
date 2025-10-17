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
#
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "boto3>=1.38.11",
#   "rich>=14.0.0",
# ]
# ///

import argparse
import os
import subprocess
import sys
from pathlib import Path

from rich.console import Console

from transfer_utils import CommonTransferUtils, convert_short_name_to_full_package_name, \
    sort_priority_packages, invalidate_cloudflare_cache

console = Console(width=200, color_system="standard")

class GithubToS3(CommonTransferUtils):
    def __init__(self, bucket, local_path):
        super().__init__(bucket, local_path)

    @staticmethod
    def fetch_commit_files(commit_ref: str, diff_filter: str="ACM"):
        console.print(f"[blue] Fetching files from last commit {commit_ref} [/]")
        cmd = [
            "git",
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "-r",
            commit_ref + "^",
            commit_ref,
            f"--diff-filter={diff_filter}"
        ]
        result = subprocess.run(cmd, check=False, capture_output=True, text=True)

        if result.returncode != 0:
            console.print(
                f"[error] Error when running diff-tree command [/]\n{result.stdout}\n{result.stderr}"
            )
            sys.exit(1)
        return result.stdout.splitlines() if result.stdout else []

    def sync_single_commit_files(self, commit_ref: str, processes: int):
        '''
        There are two parts here.
        1. When any file gets removed under docs package, we will remove from target location
        2. When any file gets added/changed/modified under docs package, we will copy from source to target location
        '''
        # Fetching `d` excludes deleted files
        # Fetching `D` includes deleted files

        files_cp_required = self.fetch_commit_files(commit_ref, diff_filter="d")
        files_del_required = self.fetch_commit_files(commit_ref, diff_filter="D")

        files_cp_required_under_docs = [f for f in files_cp_required if f.startswith("docs-archive/")]
        files_del_required_required_under_docs = [f for f in files_del_required if f.startswith("docs-archive/")]
        copy_files_pool_args = []
        delete_files_pool_args = []

        for file in files_cp_required_under_docs:
            destination_prefix = file.replace("docs-archive/", "docs/")
            dest = f"s3://{self.bucket_name}/{destination_prefix}"
            copy_files_pool_args.append((file, dest))

        for file in files_del_required_required_under_docs:
            destination_prefix = file.replace("docs-archive/", "docs/")
            dest = f"s3://{self.bucket_name}/{destination_prefix}"
            delete_files_pool_args.append(dest)

        self.run_with_pool(self.remove, delete_files_pool_args, processes=processes)
        self.run_with_pool(self.copy, copy_files_pool_args, processes=processes)

    def full_sync(self, processes: int, packages: list[str] | None = None, skip_delete: bool = False):
        if packages:
            console.print(f"[blue] Syncing packages {packages} from {self.local_path} to {self.bucket_name} [/]")
        else:
            console.print(f"[blue] Syncing all files from {self.local_path} to {self.bucket_name} [/]")
        list_of_packages = os.listdir(self.local_path) if not packages else packages
        pool_args = []
        for package in sort_priority_packages(list_of_packages):
            source = os.path.join(self.local_path, package)
            dest = f"s3://{self.bucket_name}/{self.prefix}".rstrip("/") + "/" + package
            pool_args.append((source, dest, skip_delete))

        self.run_with_pool(self.sync, pool_args, processes=processes)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync GitHub to S3")
    parser.add_argument("--bucket-path", required=True, help="S3 bucket name with path")
    parser.add_argument("--local-path", required=True, help="local path to sync")
    parser.add_argument("--document-packages", help="Document package ids to sync "
                                                   "(long or short) separated with spaces "
                                                   "('all' means all packages)", default="")
    parser.add_argument("--commit-ref", help="Commit ref to sync (sha/HEAD/branch)", default="")
    parser.add_argument("--sync-type", help="Sync type", choices=('full-sync', 'single-commit'),
                        default="single-commit")
    parser.add_argument("--processes", help="Number of processes", type=int, default=8)
    parser.add_argument("--skip-delete", help="Skip deleting missing files", action='store_true')

    args = parser.parse_args()

    syncer = GithubToS3(bucket=args.bucket_path, local_path=args.local_path)
    syncer.check_bucket()

    document_packages = args.document_packages
    # Make sure you are in the right directory for git commands
    os.chdir(Path(args.local_path).parent.as_posix())
    # Force color
    os.environ["FORCE_COLOR"] = "1"

    if document_packages != "all" and args.sync_type == "single-commit":
        console.print(f"[red] Invalid package name {document_packages} for sync type {args.sync_type} - only "
                      f"all can be used with single-commit[/]")
        sys.exit(1)

    if document_packages and document_packages != "all" and args.sync_type == "full-sync":
        packages_to_sync = []
        for _package in document_packages.split(" "):
            full_local_path = Path(f"{args.local_path}/{_package}")
            if not full_local_path.exists():
                full_local_path = Path(f"{args.local_path}/{convert_short_name_to_full_package_name(_package)}")
            if full_local_path.exists():
                console.print(f"[blue] Document package {_package} exists in bucket {args.bucket_path}.[/]")
                packages_to_sync.append(_package)
            else:
                console.print(f"[red] Document package {full_local_path} does not exist.[/]")
                sys.exit(1)
        syncer.full_sync(processes=int(args.processes), packages=packages_to_sync,
                         skip_delete=args.skip_delete)
    elif args.sync_type == "full-sync":
        syncer.full_sync(processes=int(args.processes), skip_delete=args.skip_delete)
    elif args.sync_type == "single-commit" and args.commit_ref and document_packages == "all":
        console.print(f"[blue] Syncing last commit {args.commit_ref} from {args.local_path} [/]")
        syncer.sync_single_commit_files(args.commit_ref, processes=int(args.processes))
    else:
        console.print(f"[red] Invalid sync type {args.sync_type} with document packages {document_packages} "
                      f"and commit ref {args.commit_ref}[/]")
        sys.exit(1)
    invalidate_cloudflare_cache(args.bucket_path)
