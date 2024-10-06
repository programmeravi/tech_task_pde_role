import pytest
from read_data import read_data
import os

# def test_empty_file_returns_empty_list():
#     """
#     Test that the read_data function returns an empty list 
#     when provided with a non-existent file path.
#     """
#     file_path = "data/non-existent-file.csv"
#     data = read_data(file_path)
#     assert data == []

def test_valid_file_returns_list_of_dicts():
    """
    Test that the read_data function returns a list of dictionaries 
    when provided with a valid CSV file.
    """
    file_path = "data/member-data.csv"  # Adjust if necessary
    data = read_data(file_path)

    # Assert that the data is a list
    assert isinstance(data, list)

    # Assert that each element in the list is a dictionary
    for row in data:
        assert isinstance(row, dict)

# TODO Add more tests here for different scenarios (empty CSV, invalid data, etc.)