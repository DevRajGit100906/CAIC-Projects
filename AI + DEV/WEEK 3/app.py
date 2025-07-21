from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from textblob import TextBlob
from datetime import datetime

app = Flask(__name__)

try:
    df = pd.read_csv('user_stats.csv')
    values = pd.read_csv('inferred_company_encoded_values.csv')
    model = joblib.load('like_predictor.pkl')
except Exception as e:
    print(f"Error loading files: {e}")

@app.route('/')
def home():
    return "Welcome to the Likes Predictor API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        username = data['username']
        inferred_company = data['inferred_company']
        content = data['content']
        dt = pd.to_datetime(data['Date-Time'])
        media = data['media']
        Average_Likes_Post = df[df['Username'] == username]['Average_Likes_Post'].mean()
        User_Post_Count = df[df['Username'] == username]['User_Post_Count'].mean()
        content_length = len(content)
        polarity = TextBlob(content).sentiment.polarity
        Word_Count = len(content.split())
        Release_Year = dt.year
        Is_Weekend = 1 if dt.weekday() >= 5 else 0
        Has_Mention = 1 if '<mention>' in content else 0
        Inferred_Company_Encoded = values[values['Inferred_Company'] == inferred_company]['Inferred_Company_Encoded'].values[0] if not values[values['Inferred_Company'] == inferred_company].empty else 0
        
        features = [
            Average_Likes_Post,
            User_Post_Count, 
            Word_Count,
            Inferred_Company_Encoded,
            content_length,
            Has_Mention,
            Is_Weekend,
            Release_Year,
            polarity,        
            ]
        prediction = model.predict([features])[0]
        return jsonify({'predicted_likes': int(np.expm1(prediction))})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)