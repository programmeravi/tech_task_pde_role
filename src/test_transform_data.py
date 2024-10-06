from datetime import datetime

from transform_data import transform_data


def test_full_name_combines_first_and_last_name():
    """
    Tests that the transformed data includes a FullName key with the combined first and last name (stripped).
    """
    data = [{"FirstName": "John", "LastName": "Doe"}]
    transformed_data = transform_data(data)
    assert transformed_data[0]["FullName"] == "John Doe"


def test_birth_date_formatted_if_available():
    """
    Tests that the BirthDate key is formatted as DD/MM/YYYY if available in the original data.
    """
    data = [{"BirthDate": "20001231"}]
    transformed_data = transform_data(data)
    assert transformed_data[0]["BirthDate"] == "31/12/2000"


def test_birth_date_is_none_if_not_available():
    """
    Tests that the BirthDate key is None if the corresponding key is missing from the original data.
    """
    data = [{}]
    transformed_data = transform_data(data)
    assert transformed_data[0].get("BirthDate") is None


def test_age_derived_from_birth_date():
    """
    Tests that the Age key is derived correctly from the BirthDate and reference date.
    """
    today = datetime(year=2024, month=3, day=1).date()  # Set a specific date for testing
    data = [{"BirthDate": "16031989"}]
    transformed_data = transform_data(data, today=today)
    assert transformed_data[0]["Age"] == 34


def test_salary_formatted_with_commas():
    """
    Tests that the Salary key is formatted with commas and two decimal places.
    """
    data = [{"Salary": "123456.789"}]
    transformed_data = transform_data(data)
    assert transformed_data[0]["Salary"] == "$123,456.79"


def test_salary_bucket_categorized_correctly():
    """
    Tests that the SalaryBucket key is categorized based on salary range thresholds.
    """
    data = [{"Salary": "40000"}, {"Salary": "80000"}, {"Salary": "120000"}]
    transformed_data = transform_data(data)
    assert transformed_data[0]["SalaryBucket"] == "A"
    assert transformed_data[1]["SalaryBucket"] == "B"
    assert transformed_data[2]["SalaryBucket"] == "C"


def test_address_nested_dictionary_created():
    """
    Tests that the address information is extracted and stored in a nested dictionary.
    """
    data = [
        {
            "Address": "1 Main St",
            "Suburb": "Sydney",
            "State": "NSW",
            "Post": "2000",
        }
    ]
    transformed_data = transform_data(data)
    address = transformed_data[0]["address"]
    assert address["street"] == "1 Main St"
    assert address["suburb"] == "Sydney"
    assert address["state"] == "NSW"
    assert address["postcode"] == "2000"