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
import os
from pathlib import Path

from rich.console import Console

from transfer_utils import CommonTransferUtils, convert_short_name_to_folder_name, sort_priority_folders

console = Console(width=200, color_system="standard")

import argparse
import sys


class S3TOGithub(CommonTransferUtils):

    def __init__(self, bucket:str , local_path: str):
        super().__init__(bucket, local_path)

    def verify_document_folder(self, document_folder: str):
        response= self.s3_client.list_objects_v2(
            Bucket=self.bucket_name,
            Prefix=self.prefix.rstrip("/") + "/" + document_folder,
        )
        return response["KeyCount"] > 0

    def sync_to_s3(self, processes: int, folders: list[str] | None = None):
        console.print("[blue] Syncing files from S3 to GitHub...[/]")
        prefixes = self.get_list_of_folders() if not folders else folders
        pool_args = []
        for pref in prefixes:
            source_bucket_path = f"s3://{self.bucket_name}/{pref}"
            # we want to store the files in the github under docs-archive/
            destination = self.local_path + pref.replace("docs/", "")
            pool_args.append((source_bucket_path, destination))

        self.run_with_pool(self.sync, pool_args, processes=processes)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync S3 to GitHub")
    parser.add_argument("--bucket-path", required=True, help="S3 bucket name with path")
    parser.add_argument("--local-path", required=True, help="local path to sync")
    parser.add_argument("--document-folders", help="Document folders to sync", default="all")
    parser.add_argument("--processes", help="Number of processes", type=int, default=8)

    args = parser.parse_args()

    syncer = S3TOGithub(bucket=args.bucket_path, local_path=args.local_path)
    syncer.check_bucket()
    _document_folders = args.document_folders
    # Make sure you are in the right directory for git commands
    os.chdir(Path(args.local_path).parent.as_posix())
    # Force color
    os.environ["FORCE_COLOR"] = "1"

    if _document_folders and _document_folders != "all":
        folders_to_sync = []
        for _folder in _document_folders.split(" "):
            full_folder_name = convert_short_name_to_folder_name(_folder)
            if syncer.verify_document_folder(full_folder_name):
                console.print(f"[blue] Document folder {full_folder_name} exists in bucket {args.bucket_path}.[/]")
                folders_to_sync.append(full_folder_name)
            else:
                console.print(f"[red] Document folder {full_folder_name} does not exist in bucket {args.bucket_path}.[/]")
                sys.exit(1)

        folders_to_sync = sort_priority_folders(folders_to_sync)
        syncer.sync_to_s3(processes=int(args.processes), folders=folders_to_sync)
    else:
        syncer.sync_to_s3(processes=int(args.processes))



