import subprocess
import sys
import tempfile
from functools import cached_property
from multiprocessing import Pool
from pathlib import Path
from threading import Thread
from time import sleep
from typing import Callable, Any

import boto3
import urllib3
from rich.console import Console

console = Console(width=200, color_system="standard")

def track_progress(folder: str, file_path: Path):
    while file_path.exists():
        num_lines = file_path.read_text().count("\n")
        console.print(f"{folder}: [blue] Processed {num_lines} files[/]")
        sleep(10)


class CommonTransferUtils:
    s3_client = boto3.client('s3')

    def __init__(self, bucket, local_path):
        self.bucket = bucket
        self.local_path = local_path.rstrip("/") + "/"

    @cached_property
    def bucket_name(self) -> str:
        try:
            bucket = urllib3.util.parse_url(self.bucket).netloc
            return bucket
        except Exception as e:
            console.print(f"[red] Error: {e}[/]")
            sys.exit(1)

    @cached_property
    def prefix(self) -> str:
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

    def get_list_of_folders(self) -> list[str]:
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
            return sorted(folders)
        except Exception as e:
            console.print(f"[yellow] Error: {e}[/]")
            return []


    def sync(self, source: str, destination: str):
        console.print(f"[blue] Syncing {source} to {destination} [/]")
        with tempfile.NamedTemporaryFile(mode="w+", delete=True, suffix=".out") as output_file:
            thread = Thread(target=track_progress, args=(source, Path(output_file.name),))
            thread.start()
            if source.startswith("s3://"):
                subprocess.run(
                    ["aws", "s3", "sync", "--delete", "--no-progress", source, destination],
                    stdout=output_file,
                    text=True, check=True
                )
                console.print(f"[blue] Sync completed for {source} to {destination} [/]")
            elif Path(source).is_dir():
                subprocess.run(
                    ["aws", "s3", "sync", "--delete",  "--no-progress", source, destination],
                    stdout=output_file,
                    text=True, check=True
                )
            else:
                self.copy(source, destination)
        Path(output_file.name).unlink(missing_ok=True)
        console.print(f"[blue] Sync completed for {source} to {destination} [/]")

    @staticmethod
    def run_with_pool(func: Callable, args: Any, processes: int = 4):

        with Pool(processes=processes) as pool:
            if all(isinstance(arg, tuple) for arg in args):
                pool.starmap(func, args)
            else:
                pool.map(func, args)

    @staticmethod
    def copy(source, destination):
        console.print(f"[blue] Copying {source} to {destination} [/]")
        with tempfile.NamedTemporaryFile(mode="w+", delete=True, suffix=".out") as output_file:
            thread = Thread(target=track_progress, args=(source, Path(output_file.name),))
            thread.start()
            subprocess.run(
                ["aws", "s3", "cp", "--quiet", "--no-progress", source, destination],
                stdout=output_file,
                text=True, check=True
            )
        Path(output_file.name).unlink(missing_ok=True)
        console.print(f"[blue] Copy completed for {source} to {destination} [/]")

    @staticmethod
    def remove(file_to_delete: str):
        console.print(f"[blue] Deleting {file_to_delete} [/]")
        subprocess.run(
            ["aws", "s3", "rm", file_to_delete], capture_output=True, text=True, check=True
        )
        console.print(f"[blue] Delete completed for {file_to_delete} [/]")

def convert_short_name_to_folder_name(short_name: str) -> str:
    if not short_name.startswith("apache-airflow-providers-"):
        return f"apache-airflow-providers-{short_name.replace('.', '-')}"
    return short_name

# start with those folders first
PRIORITY_FOLDERS = ["apache-airflow-providers-google", "apache-airflow-providers-amazon"]

def sort_priority_folders(folders: list[str]) -> list[str]:
    """
    Sort the folders in a way that the priority folders are at the top
    """
    sorted_folders = []
    for folder in PRIORITY_FOLDERS:
        if folder in folders:
            sorted_folders.append(folder)
            folders.remove(folder)
    return sorted_folders + sorted(folders)
