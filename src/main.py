from read_data import read_data
from transform_data import transform_data
from datetime import datetime
from dateutil.relativedelta import relativedelta

file_path = "data/member-data-smaller-sample.csv"
data = read_data(file_path)

print(type(data))
# print(data)

today_datetime = datetime(year=2024, month=3, day=1)
today = today_datetime.date()  # Extract the date part

td = []
for row in data:
    print(row)
    new_row = {}

    # clean up names 
    new_row["FirstName"] = row["FirstName"].strip()
    new_row["LastName"] = row["LastName"].strip()

    # get full name
    new_row["FullName"] = f"{new_row['FirstName']} {new_row['LastName']}"
    
    # in case if we have to handle nulls - convert BirthDate
    birth_date = row.get("BirthDate")
    if birth_date:
        new_row["BirthDate"] = datetime.strptime(birth_date, "%d%m%Y").strftime("%d/%m/%Y")
    else:
        new_row["BirthDate"] = None

    # derive age
    birth_date_str = row["BirthDate"]
    birth_date = datetime.strptime(birth_date_str, "%d%m%Y").date()
    age = relativedelta(today, birth_date).years
    new_row["Age"] = age
    
    # format salary
    float_salary = float(row.get("Salary"))
    new_row["Salary"] = f"${float_salary:,.2f}"
    td.append(new_row)

print("--" * 50)
print(td)

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