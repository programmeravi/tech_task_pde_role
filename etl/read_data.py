# import pandas as pd

# def read_data(file_path):
#     """Reads a CSV file and returns a Pandas DataFrame.

#     Args:
#         file_path (str): The path to the CSV file.

#     Returns:
#         pandas.DataFrame: The data from the CSV file as a DataFrame.
#     """

#     df = pd.read_csv(file_path, sep="|")
#     return df


import csv

def read_data(file_path):
    """Reads a CSV file and returns a list of dictionaries.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row in the CSV file.
    """

    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data