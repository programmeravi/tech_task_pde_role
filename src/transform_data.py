import pandas as pd

def transform_data(df):
    """Transforms the data in a DataFrame.

    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        pandas.DataFrame: The transformed DataFrame.
    """

    # Convert BirthDate to DD/MM/YYYY
    df['BirthDate'] = pd.to_datetime(df['BirthDate'], format='%Y-%m-%d').dt.strftime('%d/%m/%Y')

    # Format Salary with commas
    df['Salary'] = df['Salary'].apply(lambda x: f"${x:,.2f}")

    # Clean FirstName and LastName
    df['FirstName'] = df['FirstName'].str.strip()
    df['LastName'] = df['LastName'].str.strip()

    # Merge FirstName and LastName
    df['FullName'] = df['FirstName'] + ' ' + df['LastName']

    # Calculate Age
    reference_date = pd.to_datetime('2024-03-01')
    df['Age'] = (reference_date - pd.to_datetime(df['BirthDate'])).dt.days // 365

    # Create SalaryBucket
    df['SalaryBucket'] = pd.cut(df['Salary'], bins=[0, 50000, 100000, float('inf')], labels=['A', 'B', 'C'])

    # Drop unnecessary columns
    df = df.drop(columns=['FirstName', 'LastName'])

    # Create nested entity class (optional)
    # ...

    return df