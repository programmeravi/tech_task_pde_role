from read_data import read_data
from transform_data import transform_data
# from transform_data_v2 import transform_data
from datetime import datetime
# from dateutil.relativedelta import relativedelta
import json 

# # file_path = "data/member-data-smaller-sample.csv"
file_path = "data/member-data.csv"
data = read_data(file_path)
transformed_data = transform_data(data)

output_file = "transformed_json_data_full.json"

with open(output_file, 'w') as f:
    json.dump(transformed_data, f, indent=4)

# bd = "13011996"
# rs = datetime.strptime(bd, "%d%m%Y").strftime("%d/%m/%Y")
# print(rs)


# 3041976 - 30/04/1976
# 7011984 - 07/01/1984
# 13011996 - 13/01/1996
# 3021981 - this comes up with 30/02/1981 - and this results ValueError: day is out of range for month
    

# def format_birth_date(birth_date_str):
#     """
#     Formats a birth date string (if available) to DD/MM/YYYY format.
#     """
#     # print(len(birth_date_str))
#     if len(birth_date_str) <= 7:
#         birth_date_str = "0" + birth_date_str
#         return datetime.strptime(birth_date_str, "%d%m%Y").strftime("%d/%m/%Y")
#     else:
#         return datetime.strptime(birth_date_str, "%d%m%Y").strftime("%d/%m/%Y")


# print(format_birth_date("3021981"))


    # if birth_date_str:
    #     return datetime.strptime(birth_date_str, "%d%m%Y").strftime("%d/%m/%Y")
    # return None

# for row in data:
#     birth_date = row.get("BirthDate")
#     print(birth_date, type(birth_date))
#     birth_date = datetime.strptime(birth_date, "%d%m%Y").strftime("%d/%m/%Y")
#     print(birth_date, type(birth_date))

# for row in data:
#     birth_date = row.get("BirthDate")
#     result = format_birth_date(birth_date)
#     print(result)

# birth_date_str = "2061993"
# formatted_date = format_birth_date(birth_date_str)
# print(formatted_date)

# print(data)
# print("---" * 40)
# for row in data:
#     b = row.get('BirthDate')
#     print(b)
#     print(type(b))
#     r = b.strptime(b, "%d%m%Y").strftime("%d/%m/%Y")
#     print(r)
# print("---" * 40)

# print(transformed_data_sample)
# from datetime import datetime

# from transform_data import (
#     create_full_name,
#     format_birth_date,
#     calculate_age,
#     format_salary,
#     categorize_salary,
#     create_address_dict,
#     transform_data,
# )


# def test_format_birth_date():
#     """
#     Tests that the format_birth_date function formats a valid birth date string.
#     """
#     birth_date_str = "20001231"
#     formatted_date = format_birth_date(birth_date_str)
#     assert formatted_date == "31/12/2000"


# birth_date_str = 20001231
# res = birth_date_str.strptime(birth_date_str, "%d%m%Y").strftime("%d/%m/%Y")
# print(res)


# test_format_birth_date()

# class Address:
#     """
#     Represents an address with street, suburb, state, and postcode.
#     """

#     def __init__(self, street, suburb, state, postcode):
#         self.street = street
#         self.suburb = suburb
#         self.state = state
#         self.postcode = postcode


# today_datetime = datetime(year=2024, month=3, day=1) # hardcode date as its given part of assignment
# today = today_datetime.date()  # Extract the date part to derive age

# td = []
# for row in data:
#     new_row = {}
#     new_row["FullName"] = f"{row['FirstName'].strip()} {row['LastName'].strip()}"

#     # in case if we have to handle nulls - convert BirthDate
#     birth_date = row.get("BirthDate")
#     if birth_date:
#         new_row["BirthDate"] = datetime.strptime(birth_date, "%d%m%Y").strftime("%d/%m/%Y")
#     else:
#         new_row["BirthDate"] = None

#     # derive age
#     birth_date_str = row["BirthDate"]
#     birth_date = datetime.strptime(birth_date_str, "%d%m%Y").date()
#     age = relativedelta(today, birth_date).years
#     new_row["Age"] = age
    
#     # Format Salary and categorize
#     salary = float(row["Salary"].replace("$", ""))
#     new_row["Salary"] = f"${salary:,.2f}"
#     if salary < 50000:
#       new_row["SalaryBucket"] = "A"
#     elif salary < 100000:
#       new_row["SalaryBucket"] = "B"
#     else:
#       new_row["SalaryBucket"] = "C"

#     address = Address(row["Address"], row["Suburb"], row["State"], row["Post"])

#     # Extract address information and add to new_row
#     new_row["address"] = {
#         "street": address.street,
#         "suburb": address.suburb,
#         "state": address.state,
#         "postcode": address.postcode,
#     }

#     td.append(new_row)

# print("--" * 50)
# print(td)

# print(td)

# doing sample deveopment here
# sample = data[1]

# print(sample)
# print(type(data))
# print(len(data))

# transformed_data = transform_data(data)
# print(len(transformed_data))

# print(transformed_data)

# birth_date_str = sample["BirthDate"]
# print(birth_date_str)

# birth_date = datetime.datetime.strptime(birth_date_str, "%d%m%Y")
# print(birth_date)
# print(type(birth_date))
# print("--" *20)
# birth_date_req = birth_date.strftime("%d/%m/%Y")
# print(birth_date_req)
# print(type(birth_date_req))
# row["BirthDate"] = birth_date

# birth_date = sample["BirthDate"]
# birth_date_v1 = datetime.datetime.strptime(birth_date, "%d%m%Y")
# birth_date_req = birth_date_v1.strftime("%d/%m/%Y")
# # birth_date_req = datetime.datetime.strptime(birth_date, "%Y-%m-%d").strftime("%d/%m/%Y")
# print(birth_date_req)

# working code
# birth_date = sample["BirthDate"]
# birth_date_req2 = datetime.datetime.strptime(birth_date, "%d%m%Y").strftime("%d/%m/%Y")
# print(birth_date_req2)


# salary_str = "330949.2034"
# salary_float = float(salary_str)
# formatted_salary = f"${salary_float:,.2f}"
# print(formatted_salary)  # Output: $330,949.20