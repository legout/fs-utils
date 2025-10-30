from deltalake import DeltaTable
from fsspeckit.storage_options import AwsStorageOptions

# Create a StorageOptions object for S3 with a profile and allow_invalid_certificates
# This object can then be passed to libraries that accept fsspec-compatible storage options.
so_s3_polars = AwsStorageOptions.create(profile="lodl", allow_invalid_certificates=True)

# Create a DeltaTable instance from S3, passing storage options
dt_delta = DeltaTable(
    "s3://pu1/aumann/process_monitoring/results_delta",
    storage_options=so_s3_polars.to_object_store_kwargs(),
)
dt_delta.file_uris()
