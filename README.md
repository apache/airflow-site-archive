# Airflow sync archive

The repository stores the archive of generated documentation and provider registry data from Apache Airflow.

The `docs-archive/` directory contains the published documentation, and `registry-archive/` contains the
provider registry files. The `docs` and `registry` symlinks point to these directories respectively,
matching the S3 path structure used by the live and staging buckets.

The scripts and workflows here allow to keep the repository in sync with the S3 buckets - both live and
sync - where the documentation is stored. Sync in both direction is possible.

In the future we will automate synchronization of the repoitory after any change to the buckets, currently
manual synchronization S3 -> Bucket for the `live` ucket documentation is done using the `S3 to GitHub workflow`
that subsequently uses `s3-to-github.py`, and syncing the repository to the `staging` bucket is done
using the `GitHub to S3 workflow` that uses `github-to-s3.py` script. The scripts can also be used to
perform manual syncs of changes when we modify the documentation in the repository and want to
sync it to either of the S3 buckets.

You can see the arguments for the scripts in the `s3-to-github.py` and `github-to-s3.py` by passing `--help`
options:

* ``uv run scripts/s3_to_github.py --help``:

```
usage: s3_to_github.py [-h] --bucket-path BUCKET_PATH --local-path LOCAL_PATH [--document-packages DOCUMENT_PACKAGES] [--processes PROCESSES]

Sync S3 to GitHub

options:
  -h, --help            show this help message and exit
  --bucket-path BUCKET_PATH
                        S3 bucket name with path
  --local-path LOCAL_PATH
                        local path to sync
  --document-packages DOCUMENT_PACKAGES
                        Document packages to sync
  --processes PROCESSES
                        Number of processes
```

* ``uv run scripts/github_to_s3.py --help``:

```
usage: github_to_s3.py [-h] --bucket-path BUCKET_PATH --local-path LOCAL_PATH [--document-packages DOCUMENT_PACKAGES] [--commit-ref COMMIT_REF] [--sync-type {full-sync,single-commit}] [--processes PROCESSES]

Sync GitHub to S3

options:
  -h, --help            show this help message and exit
  --bucket-path BUCKET_PATH
                        S3 bucket name with path
  --local-path LOCAL_PATH
                        local path to sync
  --document-packages DOCUMENT_PACKAGES
                        Document package ids to sync (long or short) separated with spaces ('all' means all packages)
  --commit-ref COMMIT_REF
                        Commit ref to sync (sha/HEAD/branch)
  --sync-type {full-sync,single-commit}
                        Sync type
  --processes PROCESSES
                        Number of processes
```
