import pandas as pd

# Define the correct file path
file_path = r'C:\Users\DELL\Desktop\Movies.csv'

# Attempt to read the CSV file
try:
    df = pd.read_csv(file_path)
    print(df.head())
except OSError as e:
    print(f"Error: {e}")


tv_shows = df[df['Type'] == 'TV show']

shows_pe_year = tv_shows.groupby('Release_year').size()

max_year = shows_per_year.idxmax()
max_count = shows_per_year.max()

print(f"The year with the most TV shows is {max_year} with {max_count} shows.")


print(shows_per_year)





import pandas as pd

# Load your dataset
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Movies.csv")

import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Movies.csv")

import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Movies.csv")

# Print the first few rows of the DataFrame to verify
print("Data Preview:")
print(df.head())

# Print the columns to confirm their names
print("\nColumn Names:")
print(df.columns)



