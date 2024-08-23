import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\DELL\Desktop\Movies.csv')

# Count of Movies and TV Shows
type_counts = df['Type'].value_counts()

# Display the counts
print("Count of Movies and TV Shows:")
print(type_counts)
