import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess


# Load dataset
df = pd.read_csv("data/imdb_2024_movies_processed.csv")
df["Processed_Storyline"] = df["Processed_Storyline"].fillna("")

# Build TF-IDF model once
tfidf = TfidfVectorizer(max_features=5000)
tfidf_matrix = tfidf.fit_transform(df["Processed_Storyline"])


def recommend_by_storyline(user_input, top_n=5):

    # Preprocess user input
    processed_input = preprocess(user_input)

    # Transform user input into TF-IDF vector
    user_vector = tfidf.transform([processed_input])

    # Compute similarity between user input and all movies
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix)

    # Convert to list and sort
    sim_scores = list(enumerate(similarity_scores[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top N results
    top_indices = [i[0] for i in sim_scores[:top_n]]

    return df[["Movie Name", "Storyline"]].iloc[top_indices]


if __name__ == "__main__":

    print("Dataset loaded:", df.shape)

    user_story = input("\nEnter a movie storyline: ")

    recommendations = recommend_by_storyline(user_story)

    print("\nTop Recommendations:\n")
    print(recommendations)