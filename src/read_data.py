import csv

def read_data(file_path):
    """Reads a CSV file and returns a list of dictionaries.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row in the CSV file.
    """

    column_names = [
        "FirstName",
        "LastName",
        "Company",
        "BirthDate",
        "Salary",
        "Address",
        "Suburb",
        "State",
        "Post",
        "Phone",
        "Mobile",
        "Email"
    ]

    with open(file_path, 'r') as f:
        reader = csv.DictReader(f, fieldnames=column_names)
        data = [row for row in reader]
    return data