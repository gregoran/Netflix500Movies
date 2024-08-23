import pandas as pd

# File paths
file_path = 'C:/Users/DELL/Desktop/DataCamp Practice.csv'  # Ensure this matches your CSV file name
cleaned_file_path = 'C:/Users/DELL/Desktop/cleaned_data.csv'

print(f"File path being used: {file_path}")

try:
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print("Original Data:")
    print(df.head())

    # Clean the data
    # Example: Drop duplicates
    df = df.drop_duplicates()

    # Example: Fill missing values
    df = df.fillna('Unknown')

    # Save the cleaned data to a new CSV file
    df.to_csv(cleaned_file_path, index=False)

    print(f"Data has been cleaned and saved to: {cleaned_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")


