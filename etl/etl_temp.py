import os
# import pandas as pd
from read_data import read_data  # Assuming read_data is defined in read_data.py

# Get the current working directory
current_dir = os.getcwd()

# Construct the relative path to the CSV file
data_folder = "data" 
file_path = os.path.join(current_dir, data_folder, "member-data.csv")  # Join paths

# Read the data using the read_data function
try:
    data  = read_data(file_path)
    print("Data successfully read!")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
else:
    # print(df.head())  # Print the first few rows
    # print(type(data))
    # print(df[0])
    # Access the list of dictionaries
    # for row in data:
    #     # Access column values using the column names
    #     for col_name in column_names:
    #       value = row[col_name]
    #     #   print(col_name, value)
    print(type(data))
    print(data[0])