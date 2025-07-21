from flask import Flask, request, jsonify
import tweet_generator
import bonus_ai_generator

app = Flask(__name__)
simple_generator = tweet_generator.SimpleTweetGenerator()
ai_generator = bonus_ai_generator.AITweetGenerator("gpt2")

@app.route('/')
def index():
    return "Welcome to the Tweet Generator API! Use /generate to create tweets."

@app.route('/generate', methods=['POST'])
def generate_tweet():
    data = request.json
    
    company = data.get('company', 'Our Company')
    tweet_type = data.get('tweet_type', 'general')
    message = data.get('message', 'Something awesome!')
    topic = data.get('topic', 'innovation')
    
    if ai_generator.model:
        try:
            ai_tweet = ai_generator.generate_tweet(company, tweet_type, message, topic)
            return jsonify({'generator': 'ai', 'tweet': ai_tweet})
        except Exception as e:
            print({'error': f"AI generation failed: {e}"})

    simple_tweet = simple_generator.generate_tweet(
        company, 
        tweet_type, 
        message, 
        topic
    )
    return jsonify({"tweet": simple_tweet, "generator": "simple"})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'Running',
        'ai_model_loaded': bool(ai_generator.model)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)