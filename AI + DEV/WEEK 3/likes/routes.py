import pickle
import joblib
from likes import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\Users\devra\Downloads\IITD CSE LEARNING\CAIC SUMMER OF TECH\AI + DEV\WEEK 2\likes\Cleaned_Dataset.xlsx')
values = pd.read_csv(r'C:\Users\devra\Downloads\IITD CSE LEARNING\CAIC SUMMER OF TECH\AI + DEV\WEEK 2\likes\inferred_company_encoded_values.csv')
values= np.array(values)
values_company = values[:, 0]
values_encoded = values[:, 1]

class PredictionForm(FlaskForm):
    username = StringField('Username')
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
        username = form.username.data
        post_content = form.content.data
        post_datetime = form.datetime.data
        inferred_company = form.company.data
        inferred_company_encoded = int(values_encoded[list(values_company).index(inferred_company)]) if inferred_company in values_company else -1
        has_mention = int('@' in post_content or '#' in post_content)
        word_count = len(post_content.split())
        content_length = len(post_content)
        Is_weekend = int(post_datetime.lower() in ['saturday', 'sunday'])
        Release__time_year = int(post_datetime.split('-')[0])
        if username in df['Username'].values:
            Average_Likes_Post = float(df[df['Username'] == username]['Average_Likes_Post'].values[0])
            User_Post_Count = int(df[df['Username'] == username]['User_Post_Count'].values[0])
        else:
            Average_Likes_Post = 0
            User_Post_Count = 0
        
        features = {
            'Average_Likes_Post': Average_Likes_Post,
            'User_Post_Count': User_Post_Count,
            'Word_Count': word_count,
            'Inferred_Company_Encoded': inferred_company_encoded,
            'Content_Length': content_length,
            'Has_Mention': has_mention,
            'Is_Weekend': Is_weekend,
            'Release_Time_Year': Release__time_year,
        }
        print(features)
        file = r'C:\Users\devra\Downloads\IITD CSE LEARNING\CAIC SUMMER OF TECH\AI + DEV\WEEK 2\likes\like_predictor.pkl'
        model = joblib.load(file)
        features_df = pd.DataFrame([features])
        prediction = model.predict(features_df)
        prediction = int(np.exp(prediction)[0])

        return render_template('predict.html', form=form, prediction=prediction)
    return render_template('predict.html', form=form)