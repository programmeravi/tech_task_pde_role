from datetime import datetime

def transform_data(data):
  """
  Transforms a list of dictionaries representing employee data.

  Args:
      data (list): A list of dictionaries, where each dictionary represents an employee.

  Returns:
      list: A list of transformed dictionaries with additional information.
  """
  transformed_data = []

  for row in data:
    new_row = {}

    # Convert the BirthDate from the format YYYY-MM-DD to DD/MM/YYYY
    # new_row["BirthDate"] = datetime.strptime(row["BirthDate"], "%Y-%m-%d").strftime("%d/%m/%Y")

    # Handle null BirthDate with conditional formatting
    birth_date = row.get("BirthDate")  # Use get() to avoid KeyError
    if birth_date:  # Check if birth_date is not None
      new_row["BirthDate"] = datetime.strptime(birth_date, "%Y-%m-%d").strftime("%d/%m/%Y")
    else:
      new_row["BirthDate"] = None  # Assign None to BirthDate if it's null

    # new_row["FirstName"] = row["FirstName"].strip()
    # new_row["LastName"] = row["LastName"].strip()

    # # Merge names and calculate age (assuming reference date is Mar 1, 2024)
    # new_row["FullName"] = f"{new_row['FirstName']} {new_row['LastName']}"
    # birth_date = datetime.strptime(row["BirthDate"], "%d/%m/%Y")
    # reference_date = datetime(2024, 3, 1)
    # age = reference_date.year - birth_date.year - ((reference_date.month, reference_date.day) < (birth_date.month, birth_date.day))
    # new_row["Age"] = age

    # # Format Salary and categorize
    # salary = float(row["Salary"].replace("$", ""))
    # new_row["Salary"] = f"${salary:,.2f}"
    # if salary < 50000:
    #   new_row["SalaryBucket"] = "A"
    # elif salary < 100000:
    #   new_row["SalaryBucket"] = "B"
    # else:
    #   new_row["SalaryBucket"] = "C"

    # Exclude FirstName and LastName (if needed)
    # del new_row["FirstName"]
    # del new_row["LastName"]

    # Nested entity class for address (example, not implemented)
    # new_row["Address"] = Address(street=row["Address"], suburb=row["Suburb"], ...)

    transformed_data.append(new_row)

  return transformed_data

# You can use this example to test the function:
# data = [...]  # Your list of employee data
# transformed_data = transform_data(data)
# print(transformed_data)