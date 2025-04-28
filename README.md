# airflow-site-archive

### Documentation Syncing Process
### S3 To GitHub
**Sync S3 to Github**: Use the `scripts/s3_to_github.py` script to download the latest documentation from S3 to your ./docs-archive folder.
It has the following command line arguments:
- `--bucket-path`: The S3 bucket path where the documentation is stored.
- `--local-path`: The local path where the documentation will be downloaded.
- `--document-folder`: The folder in the S3 bucket where the documentation is stored (This is optional if any particular 
                      folder need to be synced, provide the folder name ex: `apache-airflow-providers-amazon`).
```bash
uv run ./scripts/s3_to_github.py.py --bucket-path s3://staging-docs-airflow-apache-org/docs/ --local-path ./docs-archive
```


### GitHub To S3
**Sync Github to S3**: Use the `scripts/github_to_s3.py` script to upload the latest documentation from your ./docs-archive folder to S3.
It has two modes:
1. **Last commit**: Syncs only last commit changes to S3.
2. **Full sync**: Syncs all files under `./docs-archive` to S3.
It has the following command line arguments:

- `--bucket-path`: The S3 bucket path where the documentation will be stored.
- `--local-path`: The local path where the documentation is stored.
- `--document-folder`: The folder in the local path where the documentation is stored (This is optional if any particular 
                      folder need to be synced, provide the folder name ex: `apache-airflow-providers-amazon`).
- `--sync-type`: The type of sync to perform. Can be either `last_commit` or `full_sync`.
- `--commit-sha`: The commit sha to sync to S3. This is only required if the sync type is `last_commit`.

```bash
uv run ./scripts/github_to_s3.py --bucket-path s3://staging-docs-airflow-apache-org/docs/ --local-path ./docs-archive --sync-type last-commit
```