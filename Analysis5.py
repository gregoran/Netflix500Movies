import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\DELL\Desktop\Movies.csv')

# Filter for movies produced in the USA
usa_movies_df = df[df['Country'].str.contains('United States', na=False)]

# Count the number of USA-produced movies
number_of_usa_movies = usa_movies_df.shape[0]

print(f"Number of movies produced in the USA: {number_of_usa_movies}")
