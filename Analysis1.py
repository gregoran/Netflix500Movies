import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Movies.csv")

# Strip any extra spaces from column names
df.columns = df.columns.str.strip()

# Check the columns again
print("Columns in the dataset:")
print(df.columns)

# Filter for TV shows
tv_shows = df[df['Type'] == 'TV Show']

# Group by Release_year and count
shows_per_year = tv_shows.groupby('Release_year').size()

# Print grouped data
print("\nShows per Year:")
print(shows_per_year)

# Find the year with the most TV shows
if not shows_per_year.empty:
    max_year = shows_per_year.idxmax()
    max_count = shows_per_year.max()

    print(f"\nThe year with the most TV shows is {max_year} with {max_count} shows.")
else:
    print("No TV shows data available.")
