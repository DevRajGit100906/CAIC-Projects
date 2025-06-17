from likes import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class PredictionForm(FlaskForm):
    content = StringField('Content of the post')
    datetime = StringField('Day and time of the post')
    company = StringField('Inferred company')
    media = StringField('Media files link (optional)')
    submit = SubmitField('Predict')

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_page():
    form = PredictionForm()
    if form.validate_on_submit():
        """post_content = form.content.data
        post_datetime = form.datetime.data
        inferred_company = form.company.data
        has_media = bool(form.media.data.strip())
        word_count = len(post_content.split())
        content_length = len(post_content)
        Is_weekend = post_datetime.lower() in ['saturday', 'sunday']
        Release__time_year = post_datetime.split('-')[0] if '-' in post_datetime else 'Unknown'"""
        
        return render_template('predict.html', form=form)
    return render_template('predict.html', form=form)