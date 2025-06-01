import streamlit as st

st.set_page_config(
    page_title="Movie Review Sentiment App",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("🎥 Movie Review Sentiment Analysis App")
st.markdown("Use the sidebar to navigate between **review submission** and **sentiment prediction**.")
st.markdown("This Application uses Naive-Bayes modelling. Its based on Bayes' Theorem. Bayes Theorem is used widely in machine learning, where it is a simple, effective way to predict classes with precision and accuracy. The Bayesian method of calculating conditional probabilities is used in machine learning applications that involve classification tasks.")
