import subprocess
import sys
from functools import cached_property
from multiprocessing import Pool

import boto3
import urllib3
from rich.console import Console

console = Console(width=200, color_system="standard")

class CommonTransferUtils:
    s3_client = boto3.client('s3')

    def __init__(self, bucket, local_path):
        self.bucket = bucket
        self.local_path = local_path.rstrip("/") + "/"

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

    def sync(self, source, destination):

        console.print(f"[blue] Syncing {source} to {destination} [/]")

        subprocess.run(
            ["aws", "s3", "sync", "--delete", source, destination], capture_output=True, text=True, check=True
        )
        console.print(f"[blue] Sync completed for {source} to {destination} [/]")

    @staticmethod
    def run_with_pool(func, args):

        with Pool(processes=4) as pool:
            pool.starmap(func, args)

    @staticmethod
    def copy(source, destination):
        console.print(f"[blue] Copying {source} to {destination} [/]")

        subprocess.run(
            ["aws", "s3", "cp", source, destination], capture_output=True, text=True, check=True
        )
        console.print(f"[blue] Copy completed for {source} to {destination} [/]")

    @staticmethod
    def remove(file_to_delete):
        console.print(f"[blue] Deleting {file_to_delete} [/]")

        subprocess.run(
            ["aws", "s3", "rm", file_to_delete], capture_output=True, text=True, check=True
        )
        console.print(f"[blue] Delete completed for {file_to_delete} [/]")
