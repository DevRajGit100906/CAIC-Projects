from flask import Flask
from flask_session import Session  # Add this import

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a_strong_secret_key_here'
app.config['SESSION_TYPE'] = 'filesystem'  # Add session config
Session(app)  # Initialize session

try:
    from tweets import routes
except Exception as e:
    print(f"Failed to import routes: {e}")