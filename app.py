from flask import Flask, render_template, request
import pandas as pd
from utils.preprocessor import apply_sentiment_model
from utils.visualizer import generate_charts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('datafile')
    if file:
        # Load and preprocess
        df = pd.read_csv(file)
        df = apply_sentiment_model(df)

        # Generate charts
        charts = generate_charts(df)

        # Convert top 5 rows to HTML table (Bootstrap style)
        sample_table = df[['Brand', 'Product_Name', 'Units_Sold', 'Rating', 'Sentiment']]\
                            .head()\
                            .to_html(classes='table table-striped table-bordered', index=False)

        # Render results
        return render_template('result.html',
                               table=sample_table,
                               graphs=charts)

    return "⚠️ No file uploaded."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
