# `fsspec_utils.utils.logging` API Reference

## `setup_logging()`

Configure the Loguru logger for fsspec-utils.

Removes the default handler and adds a new one targeting stderr with customizable level and format.

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `level` | `str`, optional | Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL). If None, uses FSSPEC_UTILS_LOG_LEVEL environment variable or defaults to "INFO". |
| `disable` | `bool` | Whether to disable logging for fsspec-utils package. |
| `format_string` | `str`, optional | Custom format string for log messages. If None, uses a default comprehensive format. |

**Returns:**

- `None`

**Example:**
```python
# Basic setup
setup_logging()

# Custom level and format
setup_logging(level="DEBUG", format_string="{time} | {level} | {message}")

# Disable logging
setup_logging(disable=True)
```

## `get_logger()`

Get a logger instance for the given name.

**Parameters:**

| Name | Type | Description |
|:---|:---|:---|
| `name` | `str` | Logger name, typically the module name. |

**Returns:**

- `Logger`: Configured logger instance.

**Example:**
```python
logger = get_logger(__name__)
logger.info("This is a log message")
```