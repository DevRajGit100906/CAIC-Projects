
# 🧠 AI & Dev Track - Week 3 Project Report

## 📌 Project Title: Tweet Like Prediction & Generation Engine

## 👨‍💻 By: Dev Raj Das  
**Track:** AI & Dev, CAIC Summer of Tech 2025  
**Week:** 3  
**Date:** July 12, 2025  

---

## 🔍 Objective
The goal of this project is to:
- Predict the number of likes a tweet will get using metadata and content features.
- Generate high-quality tweet content using both rule-based templates and AI models like GPT-2.

---

## 🗃️ Dataset Overview
- Source: `behaviour_simulation_train.csv`  
- Size: 17,331 tweets  
- Key fields: `username`, `content`, `likes`, `date`, `media`, `inferred company`  
- Shape: `(17331, 7)`
- Cleaned and saved as: `Cleaned_Dataset.xlsx`

---

## 🧼 Data Preprocessing
Key preprocessing steps:
- Converted date to datetime, extracted year/month/day/time.
- Engineered features like:
  - `Has_Mention`, `Has_Hashtag`, `Has_Url`, `Emoji_Count`, `Is_Weekend`
  - `Sentiment`, `Content_Length`, `Word_Count`
- Encoded categorical features (e.g. company name).
- Removed redundant or noisy features (`media`, `date`, etc.)
- Calculated log-transformed target: `Log_Likes`

---

## 📊 Exploratory Data Analysis
Visualized correlations between likes and features:
- `Likes vs. Sentiment`, `Content Length`, `Word Count`
- Distribution by `Month`, `Weekends`, and `Company`
- Heatmap showing `Log_Likes` correlation with key numerical features

---

## 🧠 Model Building (Likes Predictor)

### Selected Features:
- `User_Post_Count`
- `Average_Likes_Post`
- `Word_Count`
- `Inferred_Company_Encoded`
- `Content_Length`
- `Has_Mention`
- `Is_Weekend`
- `Release_Time_Year`
- `Sentiment`

### Algorithms Tested:
| Model                  | MSE   | R² Score |
|------------------------|-------|----------|
| Linear Regression      | 4.36  | 0.37     |
| Random Forest          | 0.72  | 0.90     |
| Gradient Boosting      | 0.72  | 0.90     |
| Neural Network (Keras) | 0.85  | 0.88     |
| TabNet (PyTorch)       | 1.24  | 0.82     |

✅ **Best Model:** Gradient Boosting / Random Forest  
📦 **Saved As:** `like_predictor.pkl`

---

## 🚀 Tweet Generation Module

### 1. **Rule-Based Tweet Generator**
- Found in `tweet_generator.py`
- Uses predefined templates for types: `announcement`, `question`, `general`
- Randomly selects and formats a tweet based on input values

### 2. **AI-Based Tweet Generator**
- Found in `bonus_ai_generator.py`
- Uses pre-trained GPT-2 model (`gpt2-medium`)
- Generates tweet text based on a prompt like:
  ```
  Create an announcement tweet for Nike about sports: launching new product
  ```

---

## 🌐 APIs Built

### 1. Likes Prediction API (`app.py`)
- Endpoint: `POST /predict`
- Input: JSON with tweet metadata
- Output: Predicted number of likes
- Hosted on: `localhost:5000`

### 2. Tweet Generation API (`app_generator.py`)
- Endpoint: `POST /generate`
- Input: `company`, `tweet_type`, `message`, `topic`
- Output: Generated tweet (rule-based or AI-based)
- Hosted on: `localhost:5001`

### 3. Health Check
- `GET /health` returns model status

---

## 🧪 Sample Client (`client.py`)
- Sends test POST requests to both `/predict` and `/generate` endpoints
- Handles exceptions and prints responses

---

## 🧾 Files Included

| File | Purpose |
|------|---------|
| `app.py` | Flask app for like prediction |
| `app_generator.py` | Flask app for tweet generation |
| `user_data.py` | Script to generate `user_stats.csv` |
| `tweet_generator.py` | Rule-based tweet templates |
| `bonus_ai_generator.py` | GPT-2 based tweet generation |
| `client.py` | Sample script to test APIs |
| `user_stats.csv` | Preprocessed user data |
| `inferred_company_encoded_values.csv` | Encoded company labels |
| `like_predictor.pkl` | Final trained prediction model |

---

## ✅ Summary
This project demonstrates a robust pipeline for:
- Predicting tweet popularity using metadata and NLP features
- Generating realistic tweet content using both rule-based and transformer-based approaches
- Deploying everything via clean Flask APIs for easy integration
