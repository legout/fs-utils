# `fsspec_utils.utils.types` API Reference

## `dict_to_dataframe()`

Convert a dictionary or list of dictionaries to a Polars DataFrame.

Handles various input formats: - Single dict with list values -> DataFrame rows - Single dict with scalar values -> Single row DataFrame - List of dicts with scalar values -> Multi-row DataFrame - List of dicts with list values -> DataFrame with list columns

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `data` | `dict` or `list[dict]` | The input data, either a dictionary or a list of dictionaries. |
| `unique` | `bool` | If True, duplicate rows will be removed from the resulting DataFrame. |

**Returns:**

- `polars.DataFrame`: Polars DataFrame containing the converted data.

**Examples:**
```python
# Single dict with list values
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
dict_to_dataframe(data)

# Single dict with scalar values
data = {'a': 1, 'b': 2}
dict_to_dataframe(data)

# List of dicts with scalar values
data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
dict_to_dataframe(data)
```

## `to_pyarrow_table()`

Convert various data formats to PyArrow Table.

Handles conversion from Polars DataFrames, Pandas DataFrames, dictionaries, and lists of these types to PyArrow Tables.

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `data` | `Any` | Input data to convert. |
| `concat` | `bool` | Whether to concatenate multiple inputs into single table. |
| `unique` | `bool` | If True, duplicate rows will be removed from the resulting Table. |

**Example:**

```python
import polars as pl
import pyarrow as pa
from fsspec_utils.utils.types import to_pyarrow_table

# Convert Polars DataFrame to PyArrow Table
df = pl.DataFrame({"a": [1, 2], "b": [3, 4]})
table = to_pyarrow_table(df)
print(table.schema)

# Convert list of dicts to PyArrow Table
data = [{"a": 1, "b": 10}, {"a": 2, "b": 20}]
table_from_dict = to_pyarrow_table(data)
print(table_from_dict.to_pydf())
```

**Returns:**

- `pyarrow.Table`: PyArrow Table containing the converted data.

**Example:**
```python
df = pl.DataFrame({"a": [1, 2], "b": [3, 4]})
table = to_pyarrow_table(df)
print(table.schema)
```