from read_data import read_data
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Address:
    """
    Represents an address with street, suburb, state, and postcode.
    """

    def __init__(self, street, suburb, state, postcode):
        self.street = street
        self.suburb = suburb
        self.state = state
        self.postcode = postcode


def transform_data(data):
    """
    Transforms a list of dictionaries representing employee data.

    This function adds the following key-value pairs to each dictionary:
        - FullName: Combined first and last name (stripped)
        - BirthDate: Formatted birthdate (if available)
        - Age: Derived from birthdate and reference date
        - Salary: Formatted salary with commas and two decimal places
        - SalaryBucket: Categorized based on salary range
        - address: Nested dictionary containing address components (street, suburb, state, postcode)

    Args:
        data (list): A list of dictionaries, where each dictionary represents an employee.

    Returns:
        list: A list of transformed dictionaries with additional information.
    """

    transformed_data = []
    today_datetime = datetime(year=2024, month=3, day=1)  # Reference date (hardcoded)
    today = today_datetime.date()  # Extract the date part

    for row in data:
        new_row = {}

        new_row["FullName"] = f"{row['FirstName'].strip()} {row['LastName'].strip()}"

        # Handle nulls and convert BirthDate
        birth_date = row.get("BirthDate")
        if birth_date:
            new_row["BirthDate"] = datetime.strptime(birth_date, "%d%m%Y").strftime("%d/%m/%Y")
        else:
            new_row["BirthDate"] = None

        # Derive age
        birth_date_str = row.get("BirthDate")
        if birth_date_str:
            birth_date = datetime.strptime(birth_date_str, "%d%m%Y").date()
            age = relativedelta(today, birth_date).years
            new_row["Age"] = age

        # Format Salary and categorize
        salary = float(row["Salary"].replace("$", ""))
        new_row["Salary"] = f"${salary:,.2f}"
        if salary < 50000:
            new_row["SalaryBucket"] = "A"
        elif salary < 100000:
            new_row["SalaryBucket"] = "B"
        else:
            new_row["SalaryBucket"] = "C"

        # Create and extract address information
        address = Address(row["Address"], row["Suburb"], row["State"], row["Post"])
        new_row["address"] = {
            "street": address.street,
            "suburb": address.suburb,
            "state": address.state,
            "postcode": address.postcode,
        }

        transformed_data.append(new_row)

    return transformed_data
