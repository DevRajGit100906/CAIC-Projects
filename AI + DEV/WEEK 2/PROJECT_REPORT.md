# 🧠 AI + DEV - WEEK 2 PROJECT REPORT


## 📝 Overview

This project builds upon Week 1's content-based social media post dataset. The aim of this week was to preprocess the data, extract rich features, and train regression models to predict the number of likes on a post. In addition, a complete API system was implemented using Flask, allowing users to send post information and receive a real-time prediction.

---

## 📂 Dataset Summary

- **Source File**: `behaviour_simulation_train.csv`
- **Number of Records**: 17,331
- **Initial Features**:
  - `id`, `date`, `likes`, `content`, `username`, `media`, `inferred company`

---

## 🔧 Preprocessing Pipeline

Steps performed:

1. **Cleaned and Renamed Columns**  
   Dropped `id`, converted `date` to datetime, and renamed columns for uniformity.

2. **Engineered Features**:
   - **Textual**:
     - `Content_Length`, `Word_Count`, `Sentiment` (using TextBlob)
     - `Has_Mention`, `Has_Hashtag`, `Has_Url`, `Emoji_Count`
   - **Temporal**:
     - `Release_Time_Year`, `Month`, `Day`, `Is_Weekend`, `Time_Of_Day`
   - **Categorical Encodings**:
     - `Inferred_Company_Encoded`
   - **Aggregated**:
     - `User_Post_Count`, `Average_Likes_Post`
   - **Target Transformation**:
     - `Log_Likes = log(likes + 1)` to reduce skew

3. **Removed Uninformative Features**:
   - Dropped `Has_Media` due to zero variance

---

## 🔬 Exploratory Data Analysis

Used seaborn and matplotlib to explore:

- Correlations with `Log_Likes`
- Distribution of Likes vs:
  - `Sentiment`, `Content Length`, `Word Count`
  - `Average Likes`, `User Post Count`, `Company Encoding`
- Temporal patterns: month-wise and year-wise analysis
- Boxplots and scatterplots for binary features (weekend, mention, hashtag)

---

## 📊 Final Feature Set

| Feature | Type | Description |
|--------|------|-------------|
| `Average_Likes_Post` | float | User’s average post likes |
| `User_Post_Count` | int | Total posts by user |
| `Word_Count` | int | Number of words in content |
| `Inferred_Company_Encoded` | int | Encoded company name |
| `Content_Length` | int | Length of content |
| `Has_Mention` | int | Binary feature |
| `Is_Weekend` | int | Binary feature |
| `Release_Time_Year` | int | Year extracted from datetime |
| `Sentiment` | float | Polarity score |
| `Log_Likes` | float | Target value (log of likes + 1) |

---

## 🤖 Model Training & Evaluation

Split: 75% Train / 25% Test  
Normalisation: Applied to numerical features only  
Target: `Log_Likes`

### 📈 Models Evaluated

| Model | MSE | R² Score |
|-------|-----|----------|
| Linear Regression | 4.36 | 0.37 |
| **Random Forest** | 0.72 | 0.90 |
| Gradient Boosting | **0.72** | **0.90** |
| Neural Network | 0.90 | 0.87 |
| TabNet | 1.54 | 0.78 |

🔹 **Best Model:** Gradient Boosting Regressor  
🔹 **Saved as:** `like_predictor.pkl`

---

## 🛠️ API Deployment

A Flask backend was created to serve predictions using the trained model.

### 📁 Key Files

- `app.py`: Hosts the API
- `client.py`: Sample client script to send a POST request
- `like_predictor.pkl`: Serialised trained model
- `inferred_company_encoded_values.csv`: Mapping for encoding companies
- `Cleaned_Dataset.xlsx`: Final processed dataset

### 🔘 Endpoint

**URL**: `http://127.0.0.1:5000/predict`  
**Method**: `POST`  
**Content-Type**: `application/json`

### 📥 Input Format
```json
{
  "username": "IndyMusic",
  "inferred_company": "independent",
  "content": "watch rapper <mention> freestyle for over an hour <hyperlink>",
  "Date-Time": "2018-6-30 10:04:20",
  "media": 1
}
```

### 📤 Example Output

```json
{
  "predicted_likes": 2750
}
```
