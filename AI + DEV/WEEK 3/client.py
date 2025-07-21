import requests
import time

time.sleep(2)

try:
    prediction_response = requests.post('http://localhost:5000/predict', json={
        'username': 'IndyMusic',
        'inferred_company': 'independent',
        'content': 'Check out our new album release!',
        'Date-Time': '2018-6-30 10:04:20',
        'media': 1,
    }, timeout=30)
    
    print("Predicted Likes:", prediction_response.json())
except Exception as e:
    print("Prediction failed:", str(e))

try:
    generation_response = requests.post('http://localhost:5001/generate', json={
        'company': 'Nike',
        'tweet_type': 'announcement',
        'message': 'launching new product',
        'topic': 'sports'
    }, timeout=30)
    
    print("Generated Tweet:", generation_response.json())
except Exception as e:
    print("Generation failed:", str(e))