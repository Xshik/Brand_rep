import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, accuracy_score
from textblob import TextBlob
import os

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# -------------------------------
# 1. Sales Prediction Model
# -------------------------------

def train_sales_model(csv_path='data/brand_sales_data.csv'):
    df = pd.read_csv(csv_path)

    # Encode categorical columns
    le_brand = LabelEncoder()
    le_product = LabelEncoder()
    le_category = LabelEncoder()

    df['Brand_enc'] = le_brand.fit_transform(df['Brand'])
    df['Product_enc'] = le_product.fit_transform(df['Product_Name'])
    df['Category_enc'] = le_category.fit_transform(df['Category'])

    # Features & target
    X = df[['Brand_enc', 'Product_enc', 'Category_enc', 'Rating', 'Price_Per_Unit']]
    y = df['Units_Sold']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"✅ Sales Model R² Score: {r2_score(y_test, y_pred):.2f}")

    joblib.dump(model, 'models/sales_model.pkl')
    return model

# -------------------------------
# 2. Sentiment Classification Model
# -------------------------------

def label_sentiment(text):
    score = TextBlob(str(text)).sentiment.polarity
    return 'Positive' if score > 0 else 'Negative' if score < 0 else 'Neutral'

def train_sentiment_model(csv_path='data/brand_sales_data.csv'):
    df = pd.read_csv(csv_path)

    # Add sentiment labels
    df['Sentiment_Label'] = df['Review'].apply(label_sentiment)

    # Feature extraction
    tfidf = TfidfVectorizer(max_features=500)
    X = tfidf.fit_transform(df['Review'].astype(str)).toarray()
    y = df['Sentiment_Label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = GradientBoostingClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"✅ Sentiment Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")

    joblib.dump(model, 'models/sentiment_model.pkl')
    joblib.dump(tfidf, 'models/tfidf_vectorizer.pkl')
    return model

# -------------------------------
# Call to train both models
# -------------------------------

if __name__ == '__main__':
    print("Training models... 🔧")
    train_sales_model()
    train_sentiment_model()
    print("🎉 All models trained and saved.")
