import pandas as pd
from preprocess import preprocess

# Load scraped data
df = pd.read_csv("data/imdb_2024_movies.csv")

print("Original sample:")
print(df["Storyline"].iloc[0])

# Apply preprocessing
df["Processed_Storyline"] = df["Storyline"].apply(preprocess)

print("\nProcessed sample:")
print(df["Processed_Storyline"].iloc[0])

# Save updated dataset
df.to_csv("data/imdb_2024_movies_processed.csv", index=False)

print("\nProcessed CSV saved successfully.")