import pandas as pd
import random
from faker import Faker
from datetime import timedelta, datetime

# Initialize
fake = Faker()
brands = ['Tata', 'Patanjali', 'Amul', 'Godrej', 'HUL', 'ITC']
categories = {
    'FMCG': ['Shampoo', 'Soap', 'Toothpaste'],
    'Grocery': ['Basmati Rice', 'Wheat Flour', 'Cooking Oil'],
    'Electronics': ['Smartphone', 'Smartwatch', 'Earphones']
}
reviews_pos = ['Excellent product', 'Very good quality', 'Loved it']
reviews_neg = ['Not worth the price', 'Poor quality', 'Very bad']
reviews_neu = ['Average', 'Okay product', 'Fine']

def generate_review(rating):
    if rating >= 4:
        return random.choice(reviews_pos)
    elif rating == 3:
        return random.choice(reviews_neu)
    else:
        return random.choice(reviews_neg)

data = []
start_date = datetime(2023, 1, 1)

for _ in range(100):
    cat = random.choice(list(categories.keys()))
    product = random.choice(categories[cat])
    brand = random.choice(brands)
    date = start_date + timedelta(days=random.randint(0, 365))
    units = random.randint(10, 500)
    price = round(random.uniform(50, 1500), 2)
    rating = random.choice([1, 2, 3, 4, 5])
    review = generate_review(rating)

    data.append({
        'Product_ID': f"PROD{random.randint(1000,9999)}",
        'Brand': brand,
        'Product_Name': product,
        'Category': cat,
        'Date': date.strftime('%Y-%m-%d'),
        'Units_Sold': units,
        'Rating': rating,
        'Review': review,
        'Price_Per_Unit': price
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('sample_brand_sales_data.csv', index=False)
print("✅ sample_brand_sales_data.csv created.")
