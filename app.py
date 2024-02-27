# app.py
from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("gradient_boosting_model.pkl")

# Load the benign domains
benign_df = pd.read_csv("benign_domains.csv")

# Load the malicious domains
malicious_df = pd.read_csv("malicious_domains.csv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    domain = request.form['domain']
    domain_length = len(domain)
    
    # Check if the domain is in the benign list
    if domain in benign_df['domain'].values:
        predicted_label = 'benign'
    elif domain in malicious_df['domain'].values:
        predicted_label = 'malicious'
    else:
        predicted_label = 'Sorry, the domain entered was not found in the data!'
    
    return render_template('result.html', domain=domain, predicted_label=predicted_label)

if __name__ == '__main__':
    app.run(debug=True)
