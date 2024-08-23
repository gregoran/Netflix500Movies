import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('C:/Users/DELL/Desktop/Movies.csv')

# Convert 'Duration' to numeric
df['Duration'] = pd.to_numeric(df['Duration'].str.extract('(\d+)')[0], errors='coerce')

# Plot the relationship between 'Release_year' and 'Duration'
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Release_year', y='Duration')
plt.title('Relationship between Release Year and Duration')
plt.xlabel('Release Year')
plt.ylabel('Duration (Minutes)')
plt.show()
