from read_data import read_data
from transform_data import transform_data
from datetime import datetime
import json 
# import time 

# # file_path = "data/member-data-smaller-sample.csv"
file_path = "data/member-data.csv"
data = read_data(file_path)
transformed_data = transform_data(data)

output_file = "transformed_json_data_full.json"

with open(output_file, 'w') as f:
    json.dump(transformed_data, f, indent=4)

print("successfully processed data and dumped into json !! ")

# implement infinite loop to keep the container up and running and 
# check if the transformed_json_data_full.json is in the docker container
# while True:
#     time.sleep(60)


