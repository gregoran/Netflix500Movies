import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Movies.csv")

# Strip any extra spaces from column names
df.columns = df.columns.str.strip()

# Count the number of productions by each director
director_counts = df['Director'].value_counts()

# Get the director with the most productions
top_director = director_counts.idxmax()
top_director_count = director_counts.max()

print(f"The director with the most films and TV shows is {top_director} with {top_director_count} productions.")
