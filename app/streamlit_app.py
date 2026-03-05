import streamlit as st
import sys
import os

# Allow Streamlit to import modules from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from recommender import recommend_by_storyline


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="IMDb Movie Recommender",
    layout="wide"
)

# -----------------------------
# Title & Description
# -----------------------------
st.title("IMDb Movie Recommendation System")

st.markdown(
"""
Discover movies similar to a storyline you like.

Enter a movie plot and get **Top 5 similar movies instantly.**
"""
)

# -----------------------------
# User Input
# -----------------------------
user_input = st.text_area(
    "Enter a movie storyline",
    height=180,
    placeholder="Example: An undercover detective infiltrates a powerful drug cartel..."
)

# -----------------------------
# Recommendation Button
# -----------------------------
if st.button("Recommend Movies"):

    if user_input.strip() == "":
        st.warning("Please enter a storyline first.")

    else:
        recommendations = recommend_by_storyline(user_input)

        st.subheader("⭐ Top Movie Recommendations")

        cols = st.columns(3)

        for i, (_, row) in enumerate(recommendations.iterrows()):

            with cols[i % 3]:

                st.markdown(
                    f"""
                    <div style="
                        border-radius:12px;
                        padding:18px;
                        background-color:#1e1e1e;
                        color:white;
                        margin-bottom:20px;
                        min-height:250px;
                    ">
                        <h4>🎬 {row['Movie Name']}</h4>
                        <p style="font-size:14px;">
                        {row['Storyline'][:200]}...
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built with Python, Selenium, NLP, TF-IDF, and Streamlit")