import pytest
import pymongo
from pymongo.errors import ConnectionFailure
from unittest.mock import MagicMock
from load_data_to_db import load_data_to_mongo


@pytest.fixture
def mock_mongo_client(monkeypatch):
    """Fixture to mock MongoClient."""
    mock_client = MagicMock()
    mock_db = mock_client["rnsw"]
    mock_collection = mock_db["member"]

    def raise_connection_error(*args, **kwargs):
        raise ConnectionFailure("Failed to connect to MongoDB")

    monkeypatch.setattr(pymongo.MongoClient, "__init__", raise_connection_error)

    return mock_client, mock_db, mock_collection


def test_successful_insert(mock_mongo_client):
    mock_client, mock_db, mock_collection = mock_mongo_client
    mock_collection.insert_many.return_value = {
        "inserted_ids": ["id1", "id2", "id3"]
    }

    # Sample data
    data = [{"name": "John"}, {"name": "Jane"}, {"name": "Doe"}]

    # Call the function
    inserted_count = load_data_to_mongo(data, "mongo", 27017, "rnsw", "member")

    # Assertions
    assert inserted_count == 3
    mock_collection.insert_many.assert_called_once_with(data)


def test_connection_failure(monkeypatch):    
    monkeypatch.setattr(pymongo.MongoClient, "__init__", lambda *args, **kwargs: raise ConnectionFailure("Failed to connect to MongoDB"))
    # monkeypatch.setattr(pymongo.MongoClient, "__init__", raise_connection_error)

    # Sample data
    data = [{"name": "John"}]

    # Call the function (expect exception)
    with pytest.raises(ConnectionFailure):
        load_data_to_mongo(data, "mongo", 27017, "rnsw", "member")

# TODO - further code enhancement 
# def test_insert_many_failure(mock_mongo_client):
#     mock_client, mock_db, mock_collection = mock_mongo_client
#     mock_collection.insert_many.side_effect = InvalidOperationError("Invalid operation")

#     # Sample data
#     data = [{"name": "John"}]

#     # Call the function (expect exception)
#     with pytest.raises(InvalidOperationError):
#         load_data_to_mongo(data, "mongo", 27017, "rnsw", "member")


# def test_empty_data(mock_mongo_client):
#     mock_client, mock_db, mock_collection = mock_mongo_client

#     # Sample data
#     data = []

#     # Call the function
#     inserted_count = load_data_to_mongo(data, "mongo", 27017, "rnsw", "member")

#     # Assertions
#     assert inserted_count == 0
#     mock_collection.insert_many.assert_called_once_with(data)


# def test_invalid_collection_name(mock_mongo_client):
#     mock_client, mock_db, mock_collection = mock_mongo_client
#     mock_db.return_value = None  # Mock invalid collection

#     # Sample data
#     data = [{"name": "John"}]

#     # Call the function (expect exception)
#     with pytest.raises(InvalidOperationError):
#         load_data_to_mongo(data, "mongo", 27017, "rnsw", "invalid_collection")