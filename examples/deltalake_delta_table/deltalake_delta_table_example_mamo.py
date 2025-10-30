from deltalake import DeltaTable
from fsspeckit.storage_options import AwsStorageOptions
import marimo

# Create a StorageOptions object for S3 with a profile and allow_invalid_certificates
# This object can then be passed to libraries that accept fsspec-compatible storage options.
so_s3_polars = AwsStorageOptions.create(profile="lodl", allow_invalid_certificates=True)

# Create a DeltaTable instance from S3, passing storage options
dt_delta = DeltaTable(
    "s3://pu1/aumann/process_monitoring/results_delta",
    storage_options=so_s3_polars.to_object_store_kwargs(),
)
__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    return DeltaTable, AwsStorageOptions


@app.cell
def __(AwsStorageOptions):
    # Create a StorageOptions object for S3 with a profile and allow_invalid_certificates
    # This object can then be passed to libraries that accept fsspec-compatible storage options.
    so_s3_polars = AwsStorageOptions.create(
        profile="lodl", allow_invalid_certificates=True
    )
    return (so_s3_polars,)


@app.cell
def __(DeltaTable, so_s3_polars):
    # Create a DeltaTable instance from S3, passing storage options
    dt_delta = DeltaTable(
        "s3://pu1/aumann/process_monitoring/results_delta",
        storage_options=so_s3_polars.to_object_store_kwargs(),
    )
    return (dt_delta,)


@app.cell
def __(dt_delta):
    dt_delta.file_uris()


if __name__ == "__main__":
    app.run()
