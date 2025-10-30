# `fsspec_utils.utils.misc` API Reference

## `run_parallel()`

Run a function for a list of parameters in parallel.

Provides parallel execution with progress tracking and flexible argument handling.

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `func` | `Callable` | The function to be executed in parallel. |
| `*args` | `Any` | Positional arguments to pass to `func`. If an iterable, `func` will be called for each item. |
| `n_jobs` | `int` | The number of CPU cores to use. -1 means all available cores. |
| `backend` | `str` | The backend to use for parallel processing. Options include 'loky', 'threading', 'multiprocessing', and 'sequential'. |
| `verbose` | `bool` | If True, a progress bar will be displayed during execution. |
| `**kwargs` | `Any` | Keyword arguments to pass to `func`. If an iterable, `func` will be called for each item. |

**Returns:**

- `list`: List of function outputs in the same order as inputs.

**Raises:**

- `ValueError`: If no iterable arguments provided or length mismatch.

**Examples:**
```python
# Single iterable argument
run_parallel(str.upper, ["hello", "world"])

# Multiple iterables in args and kwargs
def add(x, y, offset=0):
    return x + y + offset
run_parallel(add, [1, 2, 3], y=[4, 5, 6], offset=10)

# Fixed and iterable arguments
run_parallel(pow, [2, 3, 4], exp=2)
```

## `get_partitions_from_path()`

Extract dataset partitions from a file path.

Parses file paths to extract partition information based on different partitioning schemes.

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `path` | `str` | The file path from which to extract partition information. |
| `partitioning` | `str` or `list[str]` or `None` | The partitioning scheme to use. Can be "hive" for Hive-style, a string for a single partition column, a list of strings for multiple partition columns, or None for no specific partitioning. |

**Returns:**

- `list[tuple[str, str]]`: List of tuples containing (column, value) pairs.

**Examples:**
```python
# Hive-style partitioning
get_partitions_from_path("data/year=2023/month=01/file.parquet", "hive")

# Single partition column
get_partitions_from_path("data/2023/01/file.parquet", "year")

# Multiple partition columns
get_partitions_from_path("data/2023/01/file.parquet", ["year", "month"])
```

## `path_to_glob()`

Convert a path to a glob pattern for file matching.

Intelligently converts paths to glob patterns that match files of the specified format, handling various directory and wildcard patterns.

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `path` | `str` | The file or directory path to convert into a glob pattern. |
| `format` | `str` or `None` | The desired file format or extension to match (e.g., "parquet", "csv", "json"). If None, the format is inferred from the path. |

**Returns:**

- `str`: Glob pattern for matching files

**Example:**
```python
# Directory to parquet files glob
path_to_glob("data/", "parquet")

# Already a glob pattern
path_to_glob("data/*.csv")

# Specific file
path_to_glob("data/file.json")
```

## `check_optional_dependency()`

Check if an optional dependency is available.

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `package_name` | `str` | The name of the optional package to check for availability. |
| `feature_name` | `str` | A descriptive name of the feature that requires this package. |

**Raises:**

- `ImportError`: If the package is not available