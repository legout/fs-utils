from fsspeckit import filesystem

# --- DirFileSystem for S3 ---

# S3 Directory FileSystem for my-bucket. dirfs=True is optional, as it is often the default behavior for paths ending with a slash.
# Replace "my-bucket" with your actual S3 bucket name.
fs_dir_s3 = filesystem("s3://my-bucket", dirfs=True)

# S3 Directory FileSystem with storage_options
fs_dir_s3_so = filesystem(
    "s3://my-bucket", storage_options={"key": "your_key", "secret": "your_secret"}
)

print(f"S3 DirFileSystem (default): {fs_dir_s3}")
print(f"S3 DirFileSystem (with storage_options): {fs_dir_s3_so}")

# --- DirFileSystem for local path ---

# Local Directory FileSystem.
fs_dir_local = filesystem("./my_local_dir/", dirfs=True)

print(f"Local DirFileSystem: {fs_dir_local}")
