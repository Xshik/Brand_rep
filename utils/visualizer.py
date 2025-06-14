import plotly.express as px
import base64
from io import BytesIO

def fig_to_uri(fig):
    img = BytesIO()
    fig.write_image(img, format='png')
    encoded = base64.b64encode(img.getvalue()).decode('utf-8')
    return "data:image/png;base64," + encoded

def generate_charts(df):
    charts = {}

    # Top 10 Selling Products
    top = df.groupby('Product_Name')['Units_Sold'].sum().nlargest(10).reset_index()
    fig1 = px.bar(top, x='Product_Name', y='Units_Sold', title='Top 10 Selling Products')
    charts['top_products'] = fig_to_uri(fig1)

    # Bottom 10 Products
    bottom = df.groupby('Product_Name')['Units_Sold'].sum().nsmallest(10).reset_index()
    fig2 = px.bar(bottom, x='Product_Name', y='Units_Sold', title='Least Selling Products')
    charts['low_products'] = fig_to_uri(fig2)

    # Sentiment Distribution
    fig3 = px.pie(df, names='Sentiment', title='Customer Sentiment Distribution')
    charts['sentiments'] = fig_to_uri(fig3)

    return charts
