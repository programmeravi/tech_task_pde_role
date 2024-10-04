import os
import pandas as pd
from read_data import read_data  # Assuming read_data is defined in read_data.py

# Get the current working directory
current_dir = os.getcwd()

# Construct the relative path to the CSV file
data_folder = "data"  # Adjust if the folder name is different
file_path = os.path.join(current_dir, data_folder, "member-data.csv")  # Join paths

# Read the data using the read_data function
try:
    df = read_data(file_path)
    print("Data successfully read!")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
else:
    # print(df.head())  # Print the first few rows
    print(df)