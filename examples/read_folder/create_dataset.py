import tempfile
import shutil
import os
import polars as pl
import json


def create_sample_dataset(temp_dir):
    """Creates a sample dataset with Parquet, CSV, and JSON files."""
    print(f"\nCreating sample data in {temp_dir}")
    subdir1 = os.path.join(temp_dir, "subdir1")
    subdir2 = os.path.join(temp_dir, "subdir2")
    os.makedirs(subdir1, exist_ok=True)
    os.makedirs(subdir2, exist_ok=True)

    # Create sample data for different formats
    data1 = {"id": [1, 2], "name": ["Alice", "Bob"], "value": [10.5, 20.3]}
    data2 = {"id": [3, 4], "name": ["Charlie", "Diana"], "value": [30.7, 40.2]}

    # Write data in different formats to both subdirectories
    pl.DataFrame(data1).write_parquet(os.path.join(subdir1, "data1.parquet"))
    pl.DataFrame(data2).write_parquet(os.path.join(subdir2, "data2.parquet"))
    pl.DataFrame(data1).write_csv(os.path.join(subdir1, "data1.csv"))
    pl.DataFrame(data2).write_csv(os.path.join(subdir2, "data2.csv"))
    with open(os.path.join(subdir1, "data1.json"), "w") as f:
        json.dump(data1, f)
    with open(os.path.join(subdir2, "data2.json"), "w") as f:
        json.dump(data2, f)
    print("Sample data created.")
    return temp_dir
