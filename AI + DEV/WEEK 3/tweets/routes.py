from flask import Flask, render_template, redirect, url_for, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from tweets.tweet_generator import tweet_generator
from tweets.bonus_ai_generator import AITweetGenerator
from tweets import app


class TweetForm(FlaskForm):
    company = StringField('Company Name', render_kw={"placeholder": "Enter company name"})
    tweet_type = StringField('Tweet Type', render_kw={"placeholder": "Announcement, Question, General"})
    message = StringField('Tweet Message', render_kw={"placeholder": "Enter your message"})
    topic = StringField('Topic', render_kw={"placeholder": "Enter topic for the tweet"})
    submit = SubmitField('Generate Tweet')

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

ai = AITweetGenerator()

@app.route('/tweet', methods=['GET', 'POST'])
def tweet_page():
    form = TweetForm()
    
    # Handle form submission
    if form.validate_on_submit():
        try:
            session['generated_tweet'] = tweet_generator.generate_tweet(form)
            session['ai_generated_tweet'] = ai.generate_tweet(form)
        except Exception as e:
            print(f"Error generating tweet: {e}")
            session['generated_tweet'] = "Error generating tweet"
            session['ai_generated_tweet'] = "Error generating tweet"
        return redirect(url_for('tweet_page'))
    
    # Retrieve results from session and clear them
    generated_tweet = session.pop('generated_tweet', None)
    ai_generated_tweet = session.pop('ai_generated_tweet', None)
    
    return render_template(
        'tweet.html',
        form=form,
        generated_tweet=generated_tweet,
        ai_generated_tweet=ai_generated_tweet
    )
    