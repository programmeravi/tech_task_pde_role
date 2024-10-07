from read_data import read_data
from transform_data import transform_data
from datetime import datetime
from load_data_to_db import load_data_to_mongo
import json
# import time 

# # file_path = "data/member-data-smaller-sample.csv"
file_path = "data/member-data.csv"
data = read_data(file_path)
data_count = len(data) # if data vol is not big or done in small batches 

transformed_data = transform_data(data)
transformed_count = len(transformed_data) # if data vol is not big or done in small batches  

# write transformed_data to json file
output_file = "transformed_json_data_full.json"
with open(output_file, 'w') as f:
    json.dump(transformed_data, f, indent=4)

print("Successfully processed data and dumped into json !! ")

# MongoDB connection details
MONGO_HOST = "mongo" # TODO - get this from config - further code enhancement
MONGO_PORT = 27017

print("Uploading data to Mongo DB !!")

num_inserted = load_data_to_mongo(transformed_data, MONGO_HOST, MONGO_PORT, "rnsw", "member")
print(f"Successfully inserted {num_inserted} documents into MongoDB!")

if data_count == transformed_count and transformed_count == num_inserted:
    print("Data integrity check passed! Counts match at all stages.")
else:
    print("Data integrity check failed! Counts differ between stages.")
    print(f"Initial data count: {data_count}")
    print(f"Transformed data count: {transformed_count}")
    print(f"Documents inserted: {num_inserted}")


# implementing infinite loop to keep the container up and running and 
# check if the transformed_json_data_full.json is in the docker container
# while True:
#     time.sleep(60)




 