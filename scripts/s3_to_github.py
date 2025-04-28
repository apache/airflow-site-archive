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
#     "rich"
#     "boto3",
# ]
# ///

from rich.console import Console

console = Console(width=200, color_system="standard")

import argparse
import subprocess
import sys
from functools import cached_property
from multiprocessing import Pool

import boto3
import urllib3

class S3TOGithub:

    s3_client  = boto3.client('s3')

    def __init__(self, bucket, local_path):
        self.bucket = bucket
        self.local_path = local_path

    @cached_property
    def bucket_name(self):
        try:
            bucket = urllib3.util.parse_url(self.bucket).netloc
            return bucket
        except Exception as e:
            console.print(f"[red] Error: {e}[/]")
            sys.exit(1)

    @cached_property
    def prefix(self):
        try:
            pref = urllib3.util.parse_url(self.bucket).path
            if pref.startswith('/'):
                pref = pref[1:]
            return pref
        except Exception as e:
            console.print(f"[red] Error: {e}[/]")
            sys.exit(1)

    def check_bucket(self):
        try:
            response = self.s3_client.head_bucket(Bucket=self.bucket_name)
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                console.print(f"[blue] Bucket {self.bucket} exists.[/]")
        except Exception as e:
            console.print(f"[red] Error: {e}[/]")
            sys.exit(1)

    def verify_document_folder(self, document_folder):
        response= self.s3_client.list_objects_v2(
            Bucket=self.bucket_name,
            Prefix=self.prefix+document_folder,
        )
        return response["KeyCount"] > 0

    def get_list_of_folders(self):
        folders = []
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name,
                Prefix=self.prefix,
                Delimiter='/'
            )
            if 'CommonPrefixes' in response:
                for cur_prefix in response['CommonPrefixes']:
                    folders.append(cur_prefix['Prefix'])
            return folders
        except Exception as e:
            console.print(f"[yellow] Error: {e}[/]")
            return []

    def sync(self, bucket, bucket_prefix, destination):

        source = f"s3://{bucket}/{bucket_prefix}"

        # The source bucket folder may contain patterns like "docs/apache-airflow-providers-snowflake"
        # and we want to sync it to "docs-archive/apache-airflow-providers-snowflake"

        destination = destination.rstrip("/") + "/" + bucket_prefix.replace("docs/", "")

        console.print(f"[blue] Syncing {source} to {destination} [/]")

        subprocess.run(
            ["aws", "s3", "sync", "--delete", source, destination], capture_output=True, text=True, check=True
        )
        console.print(f"[blue] Sync completed for {source} to {destination} [/]")

    def run_sync(self):

        console.print("[blue] Syncing files from S3 to GitHub...[/]")
        prefixes = self.get_list_of_folders()

        with Pool(processes=4) as pool:
            pool.starmap(self.sync, [(self.bucket_name, doc_prefix, self.local_path) for doc_prefix in prefixes])



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync S3 to GitHub")
    parser.add_argument("--bucket-path", required=True, help="S3 bucket name with path")
    parser.add_argument("--local-path", required=True, help="local path to sync")
    parser.add_argument("--document-folder", help="Document folder to sync", default="")

    args = parser.parse_args()

    syncer = S3TOGithub(bucket=args.bucket_path, local_path=args.local_path)
    syncer.check_bucket()
    document_folder = args.document_folder

    if document_folder:
        if syncer.verify_document_folder(document_folder):
            console.print(f"[blue] Document folder {document_folder} exists in bucket {args.bucket_path}.[/]")
            syncer.sync(syncer.bucket_name, syncer.prefix+document_folder, args.local_path)
            sys.exit(0)
        else:
            console.print(f"[yellow] Document folder {document_folder} does not exist in bucket {args.bucket_path}.[/]")

    syncer.run_sync()



