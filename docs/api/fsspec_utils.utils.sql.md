# `fsspec_utils.utils.sql` API Reference

## `sql2pyarrow_filter()`

Generates a filter expression for PyArrow based on a given string and schema.

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `string` | `str` | The string containing the filter expression. |
| `schema` | `pyarrow.Schema` | The PyArrow schema used to validate the filter expression. |

**Returns:**

- `pyarrow.compute.Expression`: The generated filter expression.

**Raises:**

- `ValueError`: If the input string is invalid or contains unsupported operations.

## `sql2polars_filter()`

Generates a filter expression for Polars based on a given string and schema.

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|

| `string` | `str` | The string containing the filter expression. |
| `schema` | `polars.Schema` | The Polars schema used to validate the filter expression. |

**Returns:**

- `polars.Expr`: The generated filter expression.

**Raises:**

- `ValueError`: If the input string is invalid or contains unsupported operations.

## `get_table_names()`

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `sql_query` | `str` | The SQL query string to parse. |

**Example:**

```python
from fsspec_utils.utils.sql import get_table_names

query = "SELECT a FROM my_table WHERE b > 10"
tables = get_table_names(query)
print(tables)
# Expected: ['my_table']

query_join = "SELECT t1.a, t2.b FROM table1 AS t1 JOIN table2 AS t2 ON t1.id = t2.id"
tables_join = get_table_names(query_join)
print(tables_join)
# Expected: ['table1', 'table2']
```

**Returns:**

- `None`