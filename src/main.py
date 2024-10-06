from read_data import read_data
from transform_data import transform_data
from datetime import datetime
import json 

# # file_path = "data/member-data-smaller-sample.csv"
file_path = "data/member-data.csv"
data = read_data(file_path)
transformed_data = transform_data(data)

output_file = "transformed_json_data_full.json"

with open(output_file, 'w') as f:
    json.dump(transformed_data, f, indent=4)