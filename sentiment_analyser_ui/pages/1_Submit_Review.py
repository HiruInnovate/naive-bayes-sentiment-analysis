import streamlit as st
import json
import os

st.title("🎬 Submit a Movie Review")

# Dummy movies
movies = ["The Life of Pi", "Inception", "The Godfather"]

# Load existing data
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        reviews = json.load(f)
else:
    reviews = []

for movie in movies:
    st.subheader(movie)
    review = st.text_area(f"Your review for {movie}", key=movie)
    if st.button(f"Submit Review for {movie}", key=f"submit_{movie}"):
        if review.strip():
            reviews.append({"movie": movie, "review": review, "sentiment": ""})
            with open("data.json", "w") as f:
                json.dump(reviews, f, indent=4)
            st.success("✅ Review submitted!")
        else:
            st.warning("⚠️ Please enter a review before submitting.")
