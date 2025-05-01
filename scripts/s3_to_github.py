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

from rich.console import Console

from transfer_utils import CommonTransferUtils

console = Console(width=200, color_system="standard")

import argparse
import sys


class S3TOGithub(CommonTransferUtils):

    def __init__(self, bucket, local_path):
        super().__init__(bucket, local_path)

    def verify_document_folder(self, document_folder):
        response= self.s3_client.list_objects_v2(
            Bucket=self.bucket_name,
            Prefix=self.prefix.rstrip("/") + "/" + document_folder,
        )
        return response["KeyCount"] > 0

    def sync_to_s3(self):
        console.print("[blue] Syncing files from S3 to GitHub...[/]")
        prefixes = self.get_list_of_folders()
        pool_args = []
        for pref in prefixes:
            source_bucket_path = f"s3://{self.bucket_name}/{pref}"

            # we want to store the files in the github under docs-archive/
            destination = self.local_path + pref.replace("docs/", "")
            pool_args.append((source_bucket_path, destination))

        self.run_with_pool(self.sync, pool_args)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync S3 to GitHub")
    parser.add_argument("--bucket-path", required=True, help="S3 bucket name with path")
    parser.add_argument("--local-path", required=True, help="local path to sync")
    parser.add_argument("--document-folder", help="Document folder to sync", default="")

    args = parser.parse_args()

    syncer = S3TOGithub(bucket=args.bucket_path, local_path=args.local_path)
    syncer.check_bucket()
    document_folder = args.document_folder

    if document_folder and document_folder != "NO_DOCS":
        if syncer.verify_document_folder(document_folder):
            console.print(f"[blue] Document folder {document_folder} exists in bucket {args.bucket_path}.[/]")
            source_prefix = syncer.prefix.rstrip("/") + "/" + document_folder
            source = f"s3://{syncer.bucket_name}/{syncer.prefix}{document_folder}"
            local_path = args.local_path.rstrip("/") + "/" + document_folder
            syncer.sync(source=source, destination=local_path)
            sys.exit(0)
        else:
            console.print(f"[red] Document folder {document_folder} does not exist in bucket {args.bucket_path}.[/]")
            sys.exit(1)

    syncer.sync_to_s3()



