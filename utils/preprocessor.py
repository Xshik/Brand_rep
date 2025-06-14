import joblib
import pandas as pd

# Load the trained sentiment model and vectorizer
sentiment_model = joblib.load('models/sentiment_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

def apply_sentiment_model(df):
    # Handle missing 'Review' column
    if 'Review' not in df.columns:
        df['Review'] = "No review"
    
    # Apply the TF-IDF vectorizer and predict sentiment
    X = vectorizer.transform(df['Review'].astype(str)).toarray()
    df['Sentiment'] = sentiment_model.predict(X)
    return df
