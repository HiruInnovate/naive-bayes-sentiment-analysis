import streamlit as st
import plotly.express as px
import json
import pandas as pd
import pickle
import os

st.title("📊 Predict Sentiments of Reviews")

# Load model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Load reviews
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        reviews = json.load(f)
else:
    reviews = []

if not reviews:
    st.info("No reviews submitted yet.")
else:
    df = pd.DataFrame(reviews)

    if st.button("🔍 Predict Sentiment"):
        X = vectorizer.transform(df['review'])
        preds = model.predict(X)
        df["sentiment"] = ["Positive" if p == 1 else "Negative" for p in preds]

        # Save predictions back
        reviews = df.to_dict(orient="records")
        with open("data.json", "w") as f:
            json.dump(reviews, f, indent=4)

        st.success("✅ Predictions updated!")
        # Display table
        st.subheader("Review Sentiment Table")
        st.dataframe(df)

        sentiment_counts = df["sentiment"].value_counts().reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']  # ✅ rename to usable names



        fig = px.pie(
            sentiment_counts,
            names='Sentiment',
            values='Count',
            hole=0.4,  # 👈 this creates the donut shape
            color='Sentiment',
            color_discrete_map={'Positive': 'green', 'Negative': 'red'}
        )

        fig.update_layout(
            title_text='Sentiment Breakdown',
            paper_bgcolor='#0E1117',
            font_color='white',
            title_font_color='#08FDD8'
        )

        st.plotly_chart(fig, use_container_width=True)

        # Group by movie and sentiment
        movie_sentiment_counts = df.groupby(['movie', 'sentiment']).size().reset_index(name='count')

        # Optional: sort by total reviews per movie
        movie_sentiment_counts.sort_values(by='count', ascending=False, inplace=True)

        fig = px.bar(
            movie_sentiment_counts,
            x='count',
            y='movie',
            color='sentiment',
            orientation='h',
            title='Sentiment Distribution per Movie',
            color_discrete_map={'Positive': 'green', 'Negative': 'red'}
        )

        fig.update_layout(
            barmode='group',  # side-by-side bars
            paper_bgcolor='#0E1117',
            plot_bgcolor='#0E1117',
            font_color='white',
            title_font_color='#08FDD8',
            yaxis={'categoryorder': 'total ascending'}  # sort movies by total count
        )

        st.plotly_chart(fig, use_container_width=True)




