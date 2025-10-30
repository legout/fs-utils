# Examples Guide

This page provides an overview of the available examples in the `fsspeckit` repository. Each example is designed to be runnable and demonstrates real-world usage patterns.

## Available Examples

### Storage Configuration

**Location:** `examples/storage_options/`

Demonstrates how to create and use storage option objects for different cloud providers:

```python
from fsspeckit.storage_options import (
    LocalStorageOptions,
    AwsStorageOptions,
    GcsStorageOptions,
    AzureStorageOptions
)

# Local filesystem
local = LocalStorageOptions(auto_mkdir=True)
fs = local.to_filesystem()

# AWS S3
aws = AwsStorageOptions(
    region="us-east-1",
    access_key_id="YOUR_KEY",
    secret_access_key="YOUR_SECRET"
)
fs = aws.to_filesystem()
```

**Topics covered:**
- Creating storage options for different providers
- Converting to fsspec filesystems
- Environment variable loading
- YAML configuration

### Directory Filesystem (DirFileSystem)

**Location:** `examples/dir_file_system/`

Shows how to use DirFileSystem for treating directories as files:

```python
from fsspeckit import filesystem

# Create DirFileSystem for a directory
fs = filesystem("/data/", dirfs=True)

# Access files within the directory
files = fs.ls("/")
data = fs.cat("subdir/file.txt")
```

**Topics covered:**
- DirFileSystem creation and usage
- Path handling with directory boundaries
- Combining with storage options

### Caching

**Location:** `examples/caching/`

Demonstrates how to improve performance using the enhanced caching mechanism:

```python
from fsspeckit import filesystem

# Enable caching for S3 operations
fs = filesystem(
    "s3://my-bucket/",
    cached=True,
    cache_storage="/tmp/cache",
    verbose=True
)

# First access populates cache
data1 = fs.read_json("data.json")

# Subsequent accesses use cache (much faster!)
data2 = fs.read_json("data.json")
```

**Topics covered:**
- Cache configuration and parameters
- Performance monitoring
- Cache persistence
- Handling cache invalidation

### Batch Processing

**Location:** `examples/batch_processing/`

Shows how to process large numbers of files in batches:

```python
from fsspeckit import filesystem

fs = filesystem(".")

# Read files in batches to control memory usage
for batch_df in fs.read_csv("data/*.csv", batch_size=10):
    print(f"Processing batch with {len(batch_df)} rows")
```

**Topics covered:**
- Batch reading of multiple files
- Memory-efficient processing
- Batch aggregation
- Progress tracking

### Reading Folders

**Location:** `examples/read_folder/`

Demonstrates reading multiple files in various formats from a directory:

```python
from fsspeckit import filesystem

fs = filesystem("/data/")

# Read all Parquet files and combine
table = fs.read_parquet("**/*.parquet", concat=True)

# Read all CSV files as batches
for df in fs.read_csv("**/*.csv", batch_size=5):
    # Process each batch
    pass
```

**Topics covered:**
- Glob patterns for file discovery
- Format-specific readers
- Schema unification
- Recursive directory traversal

### S3/R2/MinIO with PyArrow Datasets

**Location:** `examples/s3_pyarrow_dataset/`

Shows how to work with partitioned datasets on object storage:

```python
from fsspeckit import filesystem
from fsspeckit.storage_options import AwsStorageOptions

# Configure for S3, Cloudflare R2, or MinIO
options = AwsStorageOptions(
    region="us-east-1",
    access_key_id="YOUR_KEY",
    secret_access_key="YOUR_SECRET"
)

fs = filesystem("s3", storage_options=options)

# Read as PyArrow dataset
dataset = fs.pyarrow_dataset("s3://bucket/data/")

# Perform efficient filtering
filtered = dataset.to_table(filter=...)
```

**Topics covered:**
- Cloud object storage configuration
- PyArrow dataset operations
- Partitioned dataset reading
- Metadata handling
- Predicate pushdown

### Delta Lake Integration

**Location:** `examples/deltalake_delta_table/`

Demonstrates integration with Delta Lake:

```python
from deltalake import DeltaTable
from fsspeckit.storage_options import LocalStorageOptions
import polars as pl

# Create sample Delta table
data = pl.DataFrame({"id": [1, 2, 3], "value": ["A", "B", "C"]})
data.write_delta("/path/to/delta_table")

# Access with fsspeckit storage options
local_opts = LocalStorageOptions()
dt = DeltaTable(
    "/path/to/delta_table",
    storage_options=local_opts.to_object_store_kwargs()
)

# Read data
table = dt.to_pyarrow_table()
```

**Topics covered:**
- Creating Delta tables
- Storage options integration
- Reading Delta metadata
- Version tracking

### PyDala Dataset

**Location:** `examples/__pydala_dataset/`

Shows how to work with Pydala datasets:

```python
from fsspeckit import filesystem

fs = filesystem(".")

# Read/write Pydala datasets
dataset = fs.pydala_dataset("/path/to/dataset")

# Access as different formats
arrow_table = dataset.to_arrow()
polars_df = dataset.to_polars()
```

**Topics covered:**
- Pydala dataset format
- Format conversions
- Dataset metadata

## Running Examples

### Prerequisites

Install fsspeckit with all optional dependencies:

```bash
pip install "fsspeckit[aws,gcp,azure]"
```

For Delta Lake examples:

```bash
pip install deltalake
```

### Execution

Most examples can be run directly:

```bash
# Run a specific example
python examples/caching/caching_example.py

# Run from Python REPL
import sys
sys.path.insert(0, '.')
exec(open('examples/dir_file_system/dir_file_system_example.py').read())

# Run with uv (if you have it installed)
uv run examples/batch_processing/batch_processing_example.py
```

### Jupyter Notebooks

Examples are available as both `.py` files and `.ipynb` Jupyter notebooks for interactive exploration:

```bash
jupyter notebook examples/s3_pyarrow_dataset/s3_pyarrow_dataset.ipynb
```

## Example Naming Conventions

- `*_example.py` - Standard Python script version
- `*_example.ipynb` - Jupyter notebook version
- `*_example_mamo.py` - Alternative implementation (if available)

## Contributing Examples

To contribute a new example:

1. Create a new subdirectory under `examples/` with a descriptive name
2. Add both `.py` and `.ipynb` versions
3. Include sample data generation if needed
4. Add docstrings explaining the example
5. Update this guide with the new example

## Quick Reference

| Use Case | Example | Key Methods |
|----------|---------|------------|
| Cloud storage access | `storage_options/` | `AwsStorageOptions.from_env()` |
| Local directory handling | `dir_file_system/` | `filesystem(..., dirfs=True)` |
| Performance optimization | `caching/` | `filesystem(..., cached=True)` |
| Large data processing | `batch_processing/` | `fs.read_csv(..., batch_size=N)` |
| Multi-format reading | `read_folder/` | `fs.read_files(..., format='auto')` |
| Object storage datasets | `s3_pyarrow_dataset/` | `fs.pyarrow_dataset(...)` |
| Data lake integration | `deltalake_delta_table/` | `DeltaTable(..., storage_options=...)` |

## Troubleshooting Examples

**Missing dependencies:** Install with `pip install "fsspeckit[aws,gcp,azure]"`

**Cloud credentials not found:** Set environment variables or update examples with credentials

**Out of memory:** Reduce batch size in batch processing examples

**Network errors:** Check connectivity to cloud services in cloud storage examples

For more help, see the [Advanced Usage](advanced.md) guide or check individual example source code.
