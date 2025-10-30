# Quickstart

This guide will help you get started with `fsspec-utils` by demonstrating how to create and interact with a directory-based filesystem for local paths.

## Installation

First, ensure you have `fsspec-utils` installed.

```bash
pip install fsspec-utils
```

## Basic Usage: Local Directory FileSystem

`fsspec-utils` simplifies working with various file systems by providing a unified interface. Here, we'll create a `DirFileSystem` for a local directory.

The `filesystem` function from `fsspec_utils` allows you to instantiate a file system object. By setting `dirfs=True`, you indicate that you want a directory-based filesystem, which treats directories as files themselves.

Let's create a local directory and then instantiate a `DirFileSystem` for it:

```python
import os
from fsspec_utils import filesystem

# Define a local directory path
local_dir_path = "./my_local_data/"

# Ensure the directory exists
os.makedirs(local_dir_path, exist_ok=True)

# Create a DirFileSystem for the local path
fs_dir_local = filesystem(local_dir_path, dirfs=True)

print(f"Local DirFileSystem created: {fs_dir_local}")

# You can now use the fs_dir_local object to interact with the directory
# For example, to list its contents (initially empty)
print(f"Contents of {local_dir_path}: {fs_dir_local.ls('/')}")

# Let's create a dummy file inside the directory
with fs_dir_local.open("test_file.txt", "w") as f:
    f.write("Hello, fsspec-utils!")

print(f"Contents after creating test_file.txt: {fs_dir_local.ls('/')}")

# Read the content of the dummy file
with fs_dir_local.open("test_file.txt", "r") as f:
    content = f.read()
print(f"Content of test_file.txt: {content}")

# Clean up the created directory and file
fs_dir_local.rm("test_file.txt")
os.rmdir(local_dir_path)
print(f"Cleaned up {local_dir_path}")
```

### Explanation

1.  **`import os` and `from fsspec_utils import filesystem`**: We import the necessary modules. `os` is used here to ensure the local directory exists, and `filesystem` is the core function from `fsspec-utils`.
2.  **`local_dir_path = "./my_local_data/"`**: We define a relative path for our local directory.
3.  **`os.makedirs(local_dir_path, exist_ok=True)`**: This line creates the `my_local_data` directory if it doesn't already exist.
4.  **`fs_dir_local = filesystem(local_dir_path, dirfs=True)`**: This is where `fsspec-utils` comes into play. We create a `DirFileSystem` instance pointing to our local directory. The `dirfs=True` argument is crucial for enabling directory-level operations.
5.  **`fs_dir_local.ls('/')`**: We use the `ls` method of our `fs_dir_local` object to list the contents of the root of our `my_local_data` directory. Initially, it will be empty.
6.  **`fs_dir_local.open("test_file.txt", "w")`**: We demonstrate writing a file within our `DirFileSystem` using the `open` method, similar to Python's built-in `open`.
7.  **`fs_dir_local.open("test_file.txt", "r")`**: We demonstrate reading the content of the file we just created.
8.  **`fs_dir_local.rm("test_file.txt")` and `os.rmdir(local_dir_path)`**: Finally, we clean up by removing the created file and the directory.

This example provides a basic overview of how to use `fsspec-utils` to interact with a local directory as a filesystem. The same `filesystem` function can be used for various other storage backends like S3, GCS, HDFS, etc., by simply changing the path and providing appropriate `storage_options`.