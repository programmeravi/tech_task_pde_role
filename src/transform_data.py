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


def create_full_name(row):
    """
    Combines the first and last name (stripped) into a FullName key.
    """
    return f"{row['FirstName'].strip()} {row['LastName'].strip()}"


def format_birth_date(birth_date_str):
    """
    Formats a birth date string (if available) to DD/MM/YYYY format.
    """
    # handle nulls
    if not birth_date_str:
        return None

    # print(len(birth_date_str))
    if len(birth_date_str) <= 7:
        birth_date_str = "0" + birth_date_str
        return datetime.strptime(birth_date_str, "%d%m%Y").strftime("%d/%m/%Y")
    else:
        return datetime.strptime(birth_date_str, "%d%m%Y").strftime("%d/%m/%Y")


def calculate_age(birth_date_str, today=datetime(year=2024, month=3, day=1).date()):
    """
    Calculates age based on the birth date string and a reference date (default: 2024-03-01).
    """
    # handle nulls
    if not birth_date_str:
        return None

    if len(birth_date_str) <= 7:
        birth_date_str = "0" + birth_date_str
        birth_date = datetime.strptime(birth_date_str, "%d%m%Y").date()
        return relativedelta(today, birth_date).years
    else:
        birth_date = datetime.strptime(birth_date_str, "%d%m%Y").date()
        return relativedelta(today, birth_date).years


def format_salary(salary):
    """
    Formats a salary value with commas and two decimal places.
    """
    if not salary or float(salary) < 0:
        return None
    
    return f"${float(salary.replace('$', '')):,.2f}"


def categorize_salary(salary):
    """
    Categorizes salary into buckets based on ranges.
    """
    if not salary:
        return None
    salary_value = float(salary.replace("$", ""))
    if salary_value < 50000:
        return "A"
    elif salary_value < 100000:
        return "B"
    else:
        return "C"


def create_address_dict(row):
    """
    Extracts address information and creates a nested dictionary.
    """
    return {
        "street": row["Address"],
        "suburb": row["Suburb"],
        "state": row["State"],
        "postcode": row["Post"],
    }


def transform_data(data):
    """
    Transforms a list of dictionaries representing employee data.

    Calls the smaller helper functions for each transformation.

    Args:
        data (list): A list of dictionaries, where each dictionary represents an employee.

    Returns:
        list: A list of transformed dictionaries with additional information.
    """

    transformed_data = []
    for row in data:
        new_row = {}
        new_row["FullName"] = create_full_name(row)
        new_row["BirthDate"] = format_birth_date(row.get("BirthDate"))
        new_row["Age"] = calculate_age(row.get("BirthDate"))
        new_row["Salary"] = format_salary(row["Salary"])
        new_row["SalaryBucket"] = categorize_salary(row["Salary"])
        new_row["address"] = create_address_dict(row)
        transformed_data.append(new_row)
    return transformed_data