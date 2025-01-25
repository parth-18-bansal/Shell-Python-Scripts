import os
from pathlib import Path

def find_largest_file(directory):
    largest_file = None
    largest_size = 0

    # Walk through the directory and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file  # Path() is used to handle different OS path conventions automatically
            file_size = file_path.stat().st_size  # Get file size in bytes

            if file_size > largest_size:
                largest_file = file_path
                largest_size = file_size

    if largest_file:
        print(f"Largest file: {largest_file}")
        print(f"Size: {largest_size}")
    else:
        print("No files found in the directory.")

# Provide the directory to search in
directory = "./"
find_largest_file(directory) 