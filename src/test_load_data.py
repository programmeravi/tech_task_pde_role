import pytest
import pymongo
from pymongo.errors import ConnectionFailure
from unittest.mock import MagicMock
from load_data_to_db import load_data_to_mongo

def test_load_data_basic():
    data = [{"name": "John"}, {"name": "Jane"}, {"name": "Doe"}]
    inserted_count = load_data_to_mongo(data, "mongo", 27017, "rnsw", "member-test")
    assert inserted_count == 3 


def test_empty_data():
    data = []
    if not data:
        pytest.skip("Skipping test for empty data")  # Skip the test
    inserted_count = load_data_to_mongo(data, "mongo", 27017, "rnsw", "member-test")
    assert inserted_count == 0

#TODO - further code enhancement , can write based on complex business req into member-test collection
