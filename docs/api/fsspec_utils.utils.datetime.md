# `fsspec_utils.utils.datetime` API Reference

## `get_timestamp_column()`

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `df` | `polars.DataFrame` | Input DataFrame. |

**Example:**

```python
import polars as pl
from fsspec_utils.utils.datetime import get_timestamp_column

df = pl.DataFrame({
    "timestamp_col": [1678886400, 1678972800],
    "value": [10, 20]
})
col_name = get_timestamp_column(df)
print(col_name)
# "timestamp_col"
```

**Returns:**

- `None`

## `get_timedelta_str()`

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `timedelta_string` | `str` | Timedelta string (e.g., "1h", "2d", "3w"). |

**Example:**

```python
from fsspec_utils.utils.datetime import get_timedelta_str

# Convert to Polars duration string
polars_duration = get_timedelta_str("1h")
print(polars_duration)
# "1h"

# Convert to Pandas timedelta string
pandas_timedelta = get_timedelta_str("2d", to="pandas")
print(pandas_timedelta)
# "2 days"
```

| `to` | `str` | Defaults to 'polars' |

**Returns:**

- `None`

## `timestamp_from_string()`

Converts a timestamp string (ISO 8601 format) into a datetime, date, or time object

using only standard Python libraries. Handles strings with or without timezone information (e.g., '2023-01-01T10:00:00+02:00', '2023-01-01', '10:00:00'). Supports timezone offsets like '+HH:MM' or '+HHMM'. For named timezones (e.g., 'Europe/Paris'), requires Python 3.9+ and the 'tzdata' package to be installed.

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `timestamp_str` | `str` | The string representation of the timestamp (ISO 8601 format). |
| `tz` | `str`, optional | Target timezone identifier (e.g., 'UTC', '+02:00', 'Europe/Paris'). If provided, the output datetime/time will be localized or converted to this timezone. Defaults to None. |
| `naive` | `bool`, optional | If True, return a naive datetime/time (no timezone info), even if the input string or `tz` parameter specifies one. Defaults to False. |

**Returns:**

- `Union[dt.datetime, dt.date, dt.time]`: The parsed datetime, date, or time object.

**Example:**

```python
from fsspec_utils.utils.datetime import timestamp_from_string

# Parse a timestamp string with timezone
dt_obj = timestamp_from_string("2023-01-01T10:00:00+02:00")
print(dt_obj)
# 2023-01-01 10:00:00+02:00

# Parse a date string
date_obj = timestamp_from_string("2023-01-01")
print(date_obj)
# 2023-01-01

# Parse a time string and localize to UTC
time_obj = timestamp_from_string("15:30:00", tz="UTC")
print(time_obj)
# 15:30:00+00:00

# Parse a timestamp and return as naive datetime
naive_dt_obj = timestamp_from_string("2023-01-01T10:00:00+02:00", naive=True)
print(naive_dt_obj)
# 2023-01-01 10:00:00
```

**Raises:**

- `ValueError`: If the timestamp string format is invalid or the timezone is invalid/unsupported.