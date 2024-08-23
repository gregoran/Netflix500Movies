import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\DELL\Desktop\Movies.csv')

# Filter for thrillers
thrillers_df = df[df['Listed_in'].str.contains('Thrillers', na=False)]

# Count the number of thrillers
number_of_thrillers = thrillers_df.shape[0]

print(f"Number of thrillers produced: {number_of_thrillers}")
