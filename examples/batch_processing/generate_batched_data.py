import tempfile
import os
import polars as pl
import json


def create_batched_dataset(temp_dir):
    """Creates a batched dataset with Parquet, CSV, and JSON files."""
    print(f"\nCreating sample data in {temp_dir}")
    sample_data = [
        {"id": i, "name": f"Name_{i}", "value": float(i * 10)} for i in range(10)
    ]

    # Create Parquet files with batched data
    for i in range(3):
        file_path = os.path.join(temp_dir, f"data_{i + 1}.parquet")
        df = pl.DataFrame(sample_data[i * 3 : (i + 1) * 3])
        df.write_parquet(file_path)
        print(f"Created Parquet file: {file_path}")

    # Create CSV files with batched data
    for i in range(3):
        file_path = os.path.join(temp_dir, f"data_{i + 1}.csv")
        df = pl.DataFrame(sample_data[i * 3 : (i + 1) * 3])
        df.write_csv(file_path)
        print(f"Created CSV file: {file_path}")

    # Create JSON files with batched data
    for i in range(3):
        file_path = os.path.join(temp_dir, f"data_{i + 1}.json")
        with open(file_path, "w") as f:
            json.dump(sample_data[i * 3 : (i + 1) * 3], f)
        print(f"Created JSON file: {file_path}")
    return temp_dir
