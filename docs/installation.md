# Installation

`fs-utils` can be installed using `pip`, the Python package installer.

## Prerequisites

- Python 3.11 or higher is required.

## Install with pip

To install `fs-utils` using `pip`, run the following command:

```bash
pip install fs-utils
```

### Optional Cloud Provider Support

Install with support for specific cloud providers:

```bash
# AWS S3 support
pip install "fs-utils[aws]"

# Google Cloud Storage support
pip install "fs-utils[gcp]"

# Azure Storage support
pip install "fs-utils[azure]"

# All cloud providers
pip install "fs-utils[aws,gcp,azure]"
```

### Upgrading

To upgrade `fs-utils` to the latest version, use:

```bash
pip install --upgrade fs-utils
```

## Environment Management with `uv` and `pixi`

For robust dependency management and faster installations, we recommend using `uv` or `pixi`.

### Using `uv`

`uv` is a fast Python package installer and resolver. To install `fsspec-utils` with `uv`:

```bash
uv pip install fs-utils
```

### Using `pixi`

`pixi` is a modern package manager for Python and other languages. To add `fsspec-utils` to your `pixi` project:

```bash
pixi add fs-utils
```

## Troubleshooting

If you encounter any issues during installation, consider the following:

- **Python Version**: Ensure you are using Python 3.11 or higher. You can check your Python version with `python --version`.
- **Virtual Environments**: It is highly recommended to use a virtual environment (e.g., `venv`, `conda`, `uv`, `pixi`) to avoid conflicts with system-wide packages.
- **Permissions**: If you encounter permission errors, you might need to run the installation command with `sudo` (e.g., `sudo pip install fsspec-utils`), but this is generally not recommended in a virtual environment.
- **Network Issues**: Check your internet connection if the installation fails to download packages.

For further assistance, please refer to the [official fs-utils GitHub repository](https://github.com/legout/fs-utils) or open an issue.