import pandas as pd
import random
from faker import Faker
from textblob import TextBlob
from datetime import timedelta, datetime

# Initialize
fake = Faker()
random.seed(42)
Faker.seed(42)

# Sample data
brands = ['Tata', 'Patanjali', 'Hindustan Unilever', 'Reliance', 'ITC', 'Amul', 'Godrej']
categories = {
    'FMCG': ['Toothpaste', 'Soap', 'Shampoo'],
    'Electronics': ['Smartphone', 'Earphones', 'Smartwatch'],
    'Grocery': ['Basmati Rice', 'Wheat Flour', 'Cooking Oil'],
}
reviews_positive = ['Very good product', 'Highly satisfied', 'Works great', 'Loved it', 'Value for money']
reviews_negative = ['Poor quality', 'Not as expected', 'Very bad experience', 'Stopped working', 'Waste of money']
reviews_neutral = ['It’s okay', 'Average product', 'Just fine', 'Not bad', 'Could be better']

# Generate data
data = []
start_date = datetime(2023, 1, 1)
for _ in range(1000):
    brand = random.choice(brands)
    category = random.choice(list(categories.keys()))
    product_name = random.choice(categories[category])
    date = start_date + timedelta(days=random.randint(0, 365))
    units_sold = random.randint(10, 500)
    rating = random.choice([1, 2, 3, 4, 5])
    price = round(random.uniform(50, 2000), 2)

    # Generate review text based on rating
    if rating >= 4:
        review = random.choice(reviews_positive)
    elif rating == 3:
        review = random.choice(reviews_neutral)
    else:
        review = random.choice(reviews_negative)

    # Sentiment using TextBlob
    sentiment_score = TextBlob(review).sentiment.polarity
    sentiment = 'Positive' if sentiment_score > 0 else 'Negative' if sentiment_score < 0 else 'Neutral'

    data.append({
        'Product_ID': f'PROD{random.randint(1000, 9999)}',
        'Brand': brand,
        'Product_Name': product_name,
        'Category': category,
        'Date': date.strftime('%Y-%m-%d'),
        'Units_Sold': units_sold,
        'Rating': rating,
        'Review': review,
        'Price_Per_Unit': price,
        'Sentiment': sentiment,
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('brand_sales_data.csv', index=False)

print("✅ brand_sales_data.csv generated successfully with 1000 records.")
