from datetime import datetime

from transform_data import (
    create_full_name,
    format_birth_date,
    calculate_age,
    format_salary,
    categorize_salary,
    create_address_dict,
    transform_data,
)


def test_create_full_name():
    """
    Tests that the create_full_name function combines first and last name (stripped).
    """
    data = {"FirstName": "John", "LastName": "Doe"}
    full_name = create_full_name(data)
    assert full_name == "John Doe"


def test_format_birth_date():
    """
    Tests that the format_birth_date function formats a valid birth date string.
    """
    birth_date_str = "2061993"
    formatted_date = format_birth_date(birth_date_str)
    assert formatted_date == "20/06/1993"


def test_format_birth_date_handles_none():
    """
    Tests that the format_birth_date function returns None for a missing birth date.
    """
    formatted_date = format_birth_date(None)
    assert formatted_date is None


def test_calculate_age():
    """
    Tests that the calculate_age function calculates the correct age.
    """
    today = datetime(year=2024, month=3, day=1).date()
    birth_date_str = "16031989"
    age = calculate_age(birth_date_str, today=today)
    assert age == 34


def test_format_salary():
    """
    Tests that the format_salary function formats a salary with commas and two decimal places.
    """
    salary_str = "123456.789"
    formatted_salary = format_salary(salary_str)
    assert formatted_salary == "$123,456.79"


def test_categorize_salary():
    """
    Tests that the categorize_salary function correctly categorizes salaries.
    """
    salary_str = "40000"
    category = categorize_salary(salary_str)
    assert category == "A"

    salary_str = "80000"
    category = categorize_salary(salary_str)
    assert category == "B"

    salary_str = "120000"
    category = categorize_salary(salary_str)
    assert category == "C"


def test_create_address_dict():
    """
    Tests that the create_address_dict function extracts address information correctly.
    """
    row = {
        "Address": "1 Main St",
        "Suburb": "Sydney",
        "State": "NSW",
        "Post": "2000",
    }
    address_dict = create_address_dict(row)
    assert address_dict["street"] == "1 Main St"
    assert address_dict["suburb"] == "Sydney"
    assert address_dict["state"] == "NSW"
    assert address_dict["postcode"] == "2000"


def test_transform_data_integrates_all_functions():
    """
    Tests that the transform_data function integrates all smaller functions correctly.
    """
    data = [
        {
            "FirstName": "John",
            "LastName": "Doe",
            "BirthDate": "2061993",
            "Salary": "123456.789",
            "Address": "1 Main St",
            "Suburb": "Sydney",
            "State": "NSW",
            "Post": "2000",
        }
    ]
    transformed_data = transform_data(data)
    assert transformed_data[0]["FullName"] == "John Doe"
    assert transformed_data[0]["BirthDate"] == "20/06/1993"
    assert transformed_data[0]["Age"] == 30
    assert transformed_data[0]["Salary"] == "$123,456.79"
    assert transformed_data[0]["SalaryBucket"] == "C"
    assert transformed_data[0]["address"]["street"] == "1 Main St"