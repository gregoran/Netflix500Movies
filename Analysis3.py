import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Movies.csv")

# Strip any extra spaces from column names
df.columns = df.columns.str.strip()

# Filter for movies listed as "Children & Family"
kids_movies = df[df['Listed_in'].str.contains('Children & Family', case=False, na=False)]

# Count the number of kids' movies
kids_movies_count = len(kids_movies)

print(f"Number of movies made for kids: {kids_movies_count}")
