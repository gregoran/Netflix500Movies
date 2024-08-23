import pandas as pd
from collections import Counter
import re

# Load the dataset
df = pd.read_csv(r'C:\Users\DELL\Desktop\Movies.csv')

# Combine all descriptions into a single string
all_descriptions = ' '.join(df['Description'].dropna().astype(str))

# Clean and tokenize the descriptions
# Remove non-alphabetic characters and convert to lowercase
words = re.findall(r'\b\w+\b', all_descriptions.lower())

# Count the frequency of each word
word_counts = Counter(words)

# Find the top 5 most common words
top_5_words = word_counts.most_common(5)

# Display the results
print("Top 5 Most Common Words in Descriptions:")
for word, count in top_5_words:
    print(f"{word}: {count}")
