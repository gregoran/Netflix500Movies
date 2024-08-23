import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\DELL\Desktop\Movies.csv')

# Convert 'Duration' to numeric, handling errors
df['Duration'] = pd.to_numeric(df['Duration'].str.extract('(\d+)')[0], errors='coerce')

# Average Duration by Genre
average_duration_by_genre = df.groupby('Listed_in')['Duration'].mean()

# Display the average duration by genre
print("Average Duration by Genre:")
print(average_duration_by_genre)

