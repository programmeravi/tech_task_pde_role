import os 
from pymongo import MongoClient

def load_data_to_mongo(data, mongo_host, mongo_port, mongo_database, mongo_collection):
  """
  This function takes transformed data and MongoDB connection details,
  inserts the data into the specified collection, and returns the number of inserted documents.
  """
  # Connect to MongoDB
  mongo_username = "root"     # os.environ.get("MONGO_INITDB_ROOT_USERNAME") # TODO - further code enhancement
  mongo_password = "password" # os.environ.get("MONGO_INITDB_ROOT_PASSWORD")

  client = MongoClient(host=mongo_host, port=mongo_port, username=mongo_username, password=mongo_password)

  db = client[mongo_database]
  collection = db[mongo_collection]

  # Insert data and get the number of inserted documents
#   inserted_count = collection.insert_many(data).inserted_count
  result = collection.insert_many(data)
  inserted_count = len(result.inserted_ids)

  # Close the connection
  client.close()

  return inserted_count