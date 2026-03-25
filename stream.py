import streamlit as st
import pandas as pd
import re
import nltk
import pickle

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split



stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|[^a-z\s]", "", text)
    tokens = text.split()
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)

@st.cache_data
def load_data():
    df = pd.read_csv("cyberbullying_tweets.csv")
    df = df[['tweet_text', 'cyberbullying_type']]
    df['label'] = df['cyberbullying_type'].apply(lambda x: 0 if x == 'not_cyberbullying' else 1)
    df['cleaned_text'] = df['tweet_text'].apply(clean_text)
    return df

@st.cache_resource
def train_models(df):
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(df['cleaned_text'])
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        "Logistic Regression": LogisticRegression(),
        "Support Vector Machine": SVC(kernel='linear', probability=True),
        "Random Forest": RandomForestClassifier(),
        "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    }

    for name in models:
        models[name].fit(X_train, y_train)

    return vectorizer, models

st.set_page_config(page_title="Cyberbullying Detector", layout="centered")
st.title("Cyberbullying Detection App")

st.markdown("This app classifies a tweet or comment as **Cyberbullying** or **Not Cyberbullying** using ML models.")

# Load data and models
with st.spinner("Loading models..."):
    df = load_data()
    vectorizer, models = train_models(df)

# User input
user_input = st.text_area("Enter a tweet or message:", height=100)

model_choice = st.selectbox("Choose a model:", list(models.keys()))

if st.button("Detect"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        model = models[model_choice]
        pred = model.predict(vectorized)[0]
        proba = model.predict_proba(vectorized)[0][pred] if hasattr(model, "predict_proba") else None

        result = "Cyberbullying" if pred == 1 else "Not Cyberbullying"
        st.markdown(result)
        if proba is not None:
            st.write(f"Confidence: **{proba:.2f}**")

# Optional: Show sample data
with st.expander("Show sample data"):
    st.dataframe(df[['tweet_text', 'cyberbullying_type']].sample(5))
