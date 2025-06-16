from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model once at startup
model = joblib.load('model/like_predictor.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array([data['Average_Likes_Post'], data['User_Post_Count'],
                         data['Word_Count'], data['Inferred_Company_Encoded'],
                         data['Content_Length'], data['Has_Mention'],
                         data['Is_Weekend'], data['Release_Time_Year']]).reshape(1, -1)
    prediction_log = model.predict(features)
    prediction = np.exp(prediction_log)
    return jsonify({'predicted_likes': float(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
