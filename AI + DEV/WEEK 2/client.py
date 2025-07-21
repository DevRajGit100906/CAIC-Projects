import requests

data = {
    "username": "IndyMusic",
    "inferred_company": "independent",
    "content": "watch rapper <mention> freestyle for over an hour <hyperlink> <hyperlink>",
    "Date-Time": "2018-6-30 10:04:20",
    "media": 1,
}

response = requests.post("http://127.0.0.1:5000/predict", json=data)

if response.status_code == 200:
    print("Predicted Likes:", response.json()['predicted_likes'])
else:
    print("Error:", response.text)