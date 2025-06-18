from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from .tweet_generator import tweet_generator
from .bonus_ai_generator import AITweetGenerator
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

@app.route('/tweet', methods=['GET', 'POST'])
def tweet_page():
    form = TweetForm()
    generated_tweet = None
    ai_generated_tweet = None
    ai = AITweetGenerator()
    
    if form.validate_on_submit():
        generated_tweet = tweet_generator.generate_tweet(
            company=form.company.data,
            tweet_type=form.tweet_type.data,
            message=form.message.data,
            topic=form.topic.data
        )
        
        # Generate AI tweet
        prompt = f"Generate a {form.tweet_type.data} tweet for {form.company.data} about {form.topic.data}: {form.message.data}"
        ai_generated_tweet = ai.generate_ai_tweet(prompt)
        
    return render_template('tweet.html', form=form, 
                         generated_tweet=generated_tweet,
                         ai_generated_tweet=ai_generated_tweet)