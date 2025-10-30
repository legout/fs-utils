# Utils Module

The `fsspeckit.utils` module provides a collection of utility functions that simplify common tasks such as logging, parallel processing, data type conversions, and schema transformations.

## Logging

### `setup_logging`

Configure logging throughout your application with loguru:

```python
from fsspeckit.utils import setup_logging

# Basic setup
setup_logging()

# With custom level and format
setup_logging(level="DEBUG", format_string="{time} | {level} | {message}")

# Control logging via environment variable
# export fsspeckit_LOG_LEVEL=DEBUG
```

**Environment Variables:**
- `fsspeckit_LOG_LEVEL` - Set the logging level (default: INFO)

## Parallel Processing

### `run_parallel`

Execute a function across multiple inputs using parallel threads with optional progress bar:

```python
from fsspeckit.utils import run_parallel

def process_file(path, multiplier=1):
    return len(path) * multiplier

results = run_parallel(
    process_file,
    ["/path1", "/path2", "/path3"],
    multiplier=2,
    n_jobs=4,
    verbose=True,  # Show progress bar
    backend="threading"
)
```

**Parameters:**
- `func` - Function to apply to each item
- `items` - List of items to process
- `n_jobs` - Number of parallel jobs (default: 1)
- `verbose` - Show progress bar (default: False)
- `backend` - Parallel backend ('threading' or 'loky')
- `**kwargs` - Additional keyword arguments passed to func

## File Synchronization

### `sync_files`

Synchronize files from source to destination, supporting efficient server-side copy when both paths are on the same filesystem:

```python
from fsspeckit.utils import sync_files

# Copy files with optional filtering
synced = sync_files(
    fs,
    source_paths=["/source/file1.txt", "/source/file2.txt"],
    target_path="/destination/",
    overwrite=True,
    verbose=True
)
```

### `sync_dir`

Recursively sync directories between filesystems:

```python
from fsspeckit.utils import sync_dir

# Sync entire directory
sync_dir(
    fs_source,
    source_path="/source/data/",
    fs_target,
    target_path="/backup/data/",
    overwrite=False,
    verbose=True
)
```

**Performance Note:** When source and target are on the same filesystem, `sync_dir` performs server-side copy for improved performance.

## Partitioning Utilities

### `get_partitions_from_path`

Extract partition information from a file path in Hive-style partition format:

```python
from fsspeckit.utils import get_partitions_from_path

# Extract partitions from path like "year=2023/month=10/day=15/data.parquet"
partitions = get_partitions_from_path("/data/year=2023/month=10/day=15/data.parquet")
# Returns: {"year": "2023", "month": "10", "day": "15"}
```

### `path_to_glob`

Convert a path with partition placeholders to a glob pattern:

```python
from fsspeckit.utils import path_to_glob

# Convert partition path to glob pattern
pattern = path_to_glob("/data/year=*/month=*/day=*/data.parquet")
# Returns: "/data/year=*/month=*/day=*/data.parquet"
```

## Type Conversion

### `dict_to_dataframe`

Convert dictionaries or lists of dictionaries to Polars DataFrame:

```python
from fsspeckit.utils import dict_to_dataframe

# Single dict
data = {"col1": [1, 2, 3], "col2": [4, 5, 6]}
df = dict_to_dataframe(data)

# List of dicts (records format)
records = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]
df = dict_to_dataframe(records)
```

### `to_pyarrow_table`

Convert various data types to PyArrow Table:

```python
from fsspeckit.utils import to_pyarrow_table

# From Polars DataFrame
table = to_pyarrow_table(polars_df)

# From Pandas DataFrame
table = to_pyarrow_table(pandas_df)

# From dictionary
data = {"col1": [1, 2, 3], "col2": [4, 5, 6]}
table = to_pyarrow_table(data)

# From list of dicts
records = [{"a": 1}, {"a": 2}]
table = to_pyarrow_table(records)
```

## Datetime Utilities

### `timestamp_from_string`

Parse timestamp strings using standard library (zoneinfo-aware):

```python
from fsspeckit.utils import timestamp_from_string
from datetime import datetime

# Parse ISO format
ts = timestamp_from_string("2023-10-15T10:30:00")

# Parse with timezone
ts = timestamp_from_string("2023-10-15T10:30:00+02:00")

# Returns: datetime object
```

### `get_timedelta_str`

Get a human-readable time difference string:

```python
from fsspeckit.utils import get_timedelta_str
from datetime import datetime

start = datetime(2023, 1, 1)
end = datetime(2023, 1, 5, 12, 30, 45)

diff_str = get_timedelta_str(start, end)
# Returns: "4 days 12:30:45" (or similar format)
```

## Data Type Optimization

### Polars Data Type Optimization

#### `opt_dtype`

Automatically optimize Polars column data types to reduce memory usage:

```python
from fsspeckit.utils import opt_dtype_pl
import polars as pl

# Optimize a single column
df = pl.DataFrame({"id": [1, 2, 3], "count": [100, 200, 300]})
optimized = opt_dtype_pl(df)

# Or use as DataFrame extension:
df_opt = df.opt_dtype  # Custom extension method
```

**Optimizations include:**
- Int64 → Int32 when range fits
- Float64 → Float32 when precision allows
- Large string → small string
- Categorical encoding for repetitive strings

#### `opt_dtype_pa`

PyArrow equivalent for type optimization:

```python
from fsspeckit.utils import opt_dtype_pa

# Optimize PyArrow table
table = pa.table({"id": [1, 2, 3], "count": [100, 200, 300]})
optimized = opt_dtype_pa(table)
```

## Schema Utilities

### `cast_schema`

Unify schemas across multiple tables/dataframes:

```python
from fsspeckit.utils import cast_schema

# Cast one schema to match another
target_schema = table1.schema
cast_table2 = cast_schema(table2, target_schema)
```

### `convert_large_types_to_normal`

Convert large_string/large_binary to normal string/binary types:

```python
from fsspeckit.utils import convert_large_types_to_normal

# Convert large types in PyArrow table
table = convert_large_types_to_normal(table)

# Useful for compatibility with systems that don't support large types
```

## SQL-to-Expression Conversion

### `sql2pyarrow_filter`

Convert SQL WHERE clause to PyArrow filter expression:

```python
from fsspeckit.utils import sql2pyarrow_filter
import pyarrow as pa

# Define schema
schema = pa.schema([
    ("age", pa.int32()),
    ("name", pa.string()),
    ("date", pa.timestamp("us"))
])

# Create filter from SQL
expr = sql2pyarrow_filter(
    "age > 25 AND name = 'Alice'",
    schema
)

# Apply to dataset
filtered = dataset.to_table(filter=expr)
```

### `sql2polars_filter`

Convert SQL WHERE clause to Polars filter expression:

```python
from fsspeckit.utils import sql2polars_filter

# Create filter expression
expr = sql2polars_filter("age > 25 AND status = 'active'")

# Apply to DataFrame
filtered_df = df.filter(expr)
```

**Supported SQL syntax:**
- Comparison operators: `>`, `<`, `>=`, `<=`, `=`, `!=`
- Logical operators: `AND`, `OR`, `NOT`
- In operator: `IN (val1, val2)`
- Between operator: `BETWEEN x AND y`
- Null checks: `IS NULL`, `IS NOT NULL`

## Dependency Checking

### `check_optional_dependency`

Verify that optional dependencies are installed:

```python
from fsspeckit.utils import check_optional_dependency

# Check for a dependency
try:
    check_optional_dependency("polars")
except ImportError as e:
    print(f"Optional dependency missing: {e}")
```

## Filesystem Comparison

### `check_fs_identical`

Compare two filesystems to verify they contain identical data:

```python
from fsspeckit.utils import check_fs_identical

# Compare local directories
fs1 = filesystem("/path1")
fs2 = filesystem("/path2")

identical = check_fs_identical(fs1, "/data", fs2, "/data")
```

## Polars DataFrame Extensions

When using fsspeckit with Polars, additional methods are automatically added to DataFrames:

```python
import polars as pl
from fsspeckit import filesystem

df = pl.DataFrame({
    "date": ["2023-01-01", "2023-02-15"],
    "category": ["A", "B"],
    "value": [100, 200]
})

# Access optimized dtypes
df_opt = df.opt_dtype

# Create partition columns from date
df_with_parts = df.with_datepart_columns("date")

# Drop columns with all null values
df_clean = df.drop_null_columns()
```
