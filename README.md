# 🎬 Naive Bayes Sentiment Analysis

This repository demonstrates how to build a **Sentiment Classifier** using the **IMDB 50K Movie Reviews Dataset**. It covers the full journey from understanding the fundamentals of **Supervised Learning** and **Naive Bayes**, to building a production-ready **Streamlit web app** that predicts the sentiment of user-submitted movie reviews.

---

## 📌 Table of Contents

- [🔍 Problem Statement](#-problem-statement)
- [📚 Concepts Covered](#-concepts-covered)
- [🧪 Model Training (Jupyter Notebook)](#-model-training-jupyter-notebook)
- [🖥️ Streamlit App](#️-streamlit-app)
- [📊 Visualizations](#-visualizations)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 How to Run](#-how-to-run)
- [📦 Dataset](#-dataset)


---

## 🔍 Problem Statement

Can we automatically determine the **sentiment (positive or negative)** of a movie review using machine learning?

This project uses **Naive Bayes**, a probabilistic classifier, to predict sentiments based on text input.

---

## 📚 Concepts Covered

- What is **Supervised Learning**?
- What is **Classification**?
- Introduction to **Bayes' Theorem**
- Extension to **Naive Bayes Classifier**
- How Naive Bayes fits **Sentiment Analysis**
- Feature extraction using **Bag of Words** via `CountVectorizer`
- Building and testing using **ComplementNB**

---

## 🧪 Model Training (Jupyter Notebook)

- Data Cleaning & Preprocessing
- Stopword Removal
- Tokenization using Regex
- Feature Extraction using CountVectorizer
- Model training using `ComplementNB`
- Evaluation (Accuracy, Confusion Matrix)

➡️ Notebook: `SentimentAnalysisWithNaiveBayes.ipynb`

---

## 🖥️ Streamlit App
Folder: sentiment_analyser_ui
An interactive UI to:
- Submit a review on a movie card
- Click "Predict" to see real-time sentiment
- View review and prediction in a table
- See sentiment distribution using horizontal bar chart

➡️ App file: `sentiment_analyser_ui/streamlit_app.py`
Install dependencies after creating virtual environment:
```bash
pip install -r requirements.txt
```


Run with command:
```bash
streamlit run streamlit_app.py
```

---

## 📊 Visualizations

- Bar charts showing sentiment distribution
- Tabular summary of predictions
- Clean and dark-themed interface

---

## 🛠️ Tech Stack

- Python
- Pandas, Numpy, Scikit-learn
- NLTK & spaCy
- Streamlit
- Matplotlib / Plotly

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/HiruInnovate/naive-bayes-sentiment-analysis.git
cd naive-bayes-sentiment-analysis
```
### 2. Run the Notebook
### 3. In sentiment_analyser_ui, install the requirements
### 4. Copy the model binary file and the count vectorizer binary file into this folder
### 5. Run the main app by using command
```bash
streamlit run streamlit_app.py
```
## Dataset
IMDB dataset having 50K movie reviews for natural language processing or Text analytics. This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. We provide a set of 25,000 highly polar movie reviews for training and 25,000 for testing.

# About me
I am `Hiranmoy Goswami`, I am passionate about `AI/ML/DL` , `Generative AI applications` and their use in different domains, I also love to build `web applications` using `Java, React`, I have backend development experience with Java[Microservices]. For any work, you can reach out to me at...

* [LinkedIn](https://www.linkedin.com/in/hiranmoy-goswami-1997-dev/)
* [Youtube](https://www.youtube.com/channel/UCzQ9e6BsI1XiBWD3wlBRfrQ)