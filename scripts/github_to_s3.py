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
#     "rich",
#     "boto3",
# ]
# ///

import argparse
import os
import subprocess
import sys
from pathlib import Path

from rich.console import Console

from transfer_utils import CommonTransferUtils

console = Console(width=200, color_system="standard")

class GithubToS3(CommonTransferUtils):
    def __init__(self, bucket, local_path):
        super().__init__(bucket, local_path)

    @staticmethod
    def fetch_last_commit_files(commit_sha, diff_filter="ACM"):
        console.print(f"[blue] Fetching files from last commit {commit_sha} [/]")
        cmd = [
            "git",
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "-r",
            commit_sha + "^",
            commit_sha,
            f"--diff-filter={diff_filter}"
        ]
        result = subprocess.run(cmd, check=False, capture_output=True, text=True)
        console.print(f"[blue] Running command: {' '.join(cmd)} [/]")
        console.print(f"[blue] Result: {result.stdout} [/]")
        console.print(f"[blue] Error: {result.stderr} [/]")
        console.print(f"[blue] Return code: {result.returncode} [/]")

        if result.returncode != 0:
            console.print(
                f"[warning] Error when running diff-tree command [/]\n{result.stdout}\n{result.stderr}"
            )
            return []
        return result.stdout.splitlines() if result.stdout else []

    def sync_last_commit_files(self, commit_sha: str):
        '''
        There are two parts here.
        1. When any file gets removed under docs folder, we will remove from target location
        2. When any file gets added/changed/modified under docs folder, we will copy from source to target location
        '''
        # Fetching `d` excludes deleted files
        # Fetching `D` includes deleted files

        files_cp_required = self.fetch_last_commit_files(commit_sha, diff_filter="d")
        files_del_required = self.fetch_last_commit_files(commit_sha, diff_filter="D")

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

        self.run_with_pool(self.remove, delete_files_pool_args)
        self.run_with_pool(self.copy, copy_files_pool_args)

    def full_sync(self):
        console.print(f"[blue] Syncing all files from {self.local_path} to {self.bucket_name} [/]")
        list_of_folders = os.listdir(self.local_path)
        pool_args = []
        for folder in list_of_folders:
            source = os.path.join(self.local_path, folder)
            dest = f"s3://{self.bucket_name}/{self.prefix}".rstrip("/") + "/" + folder
            pool_args.append((source, dest))

        self.run_with_pool(self.sync, pool_args)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync GitHub to S3")
    parser.add_argument("--bucket-path", required=True, help="S3 bucket name with path")
    parser.add_argument("--local-path", required=True, help="local path to sync")
    parser.add_argument("--document-folder", help="Document folder to sync", default="")
    parser.add_argument("--commit-sha", help="Commit SHA to sync", default="")
    parser.add_argument("--sync-type", help="Sync type", default="last_commit")

    args = parser.parse_args()

    syncer = GithubToS3(bucket=args.bucket_path, local_path=args.local_path)
    syncer.check_bucket()

    document_folder = args.document_folder

    if document_folder and document_folder != "NO_DOCS":
        full_local_path = Path(f"{args.local_path}/{document_folder}")
        if full_local_path.exists():
            console.print(f"[blue] Document folder {document_folder} exists in bucket {args.bucket_path}.[/]")

            destination = f"s3://{syncer.bucket_name}/{syncer.prefix}".rstrip("/") + "/" + document_folder
            syncer.sync(source=full_local_path, destination=destination)
            sys.exit(0)
        else:
            console.print(f"[red] Document folder {document_folder} does not exist in github {args.local_path}.[/]")
            sys.exit(1)

    if args.sync_type == "last_commit" and args.commit_sha:
        console.print(f"[blue] Syncing last commit {args.commit_sha} from {args.local_path} [/]")
        syncer.sync_last_commit_files(args.commit_sha)
        sys.exit(0)

    if args.sync_type == "full_sync":
        syncer.full_sync()
        sys.exit(0)

    console.print(f"[red] Invalid sync type {args.sync_type} [/]")

