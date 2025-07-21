# AI + DEV - WEEK 1 PROJECT REPORT


## 🧠 Problem Statement

We are given a dataset containing user-generated content with metadata such as likes, usernames, media, and inferred companies. The goal is to perform comprehensive data analysis and feature engineering to prepare the data for modeling a system that can predict the number of likes a post will receive. Additionally, an API is to be designed to take post information and predict likes, while offering suggestions to improve engagement.

---

## 📂 Dataset Overview

- **File Shape:** (17,331 rows × 7 columns)
- **Columns:**
  - `id`, `date`, `likes`, `content`, `username`, `media`, `inferred company`

---

## ⚙️ Steps Performed

### 1. **Data Loading**
- Loaded the dataset from a CSV file (`behaviour_simulation_train.xlsx - Sheet1.csv`)
- Verified integrity: no null values, no duplicates.

### 2. **Light Preprocessing**
- Dropped unnecessary columns (`media`, `date`)
- Converted date column to datetime and extracted temporal features:
  - `year`, `month`, `day`, `hour`, `minute`, `second`, `time_of_day`, `is_weekend`
- Created binary columns:
  - `has_media`, `has_mention`
- Text cleaning and processing (`content` column)
- Added new content features:
  - `content_length`, `word_count`
- Aggregated user statistics:
  - `user_post_count`, `average_likes_post`
- Encoded categorical variables (e.g., `inferred_company_encoded`)
- Final dataset shape: **(17,331 rows × 15 columns)**

### 3. **Exploratory Data Analysis (EDA)**
Visualizations and insights generated:
- **Histograms & Boxplots:** Distribution of likes
- **Scatterplots:** 
  - `content_length` vs `likes`
  - `word_count` vs `likes`
  - `user_post_count` vs `likes`
  - `average_likes_post` vs `likes`
- **Categorical Analysis:**
  - `is_weekend` vs `likes`
  - `has_media` vs `likes`
  - `has_mention` vs `likes`
- **Time Trends:** 
  - Year-wise like trends
  - Monthly distribution
- **Company Influence:** 
  - `inferred_company_encoded` vs `likes`

---

## 📊 Final Features Used

| Feature | Description |
|--------|-------------|
| `user_post_count` | Total posts by user |
| `average_likes_post` | Mean likes per post by user |
| `content` | Post content |
| `word_count` | Number of words |
| `content_length` | Total characters |
| `has_media` | Boolean for presence of media |
| `has_mention` | Boolean for presence of `<mention>` |
| `release_time_year` | Year of post |
| `release_time_month` | Month of post |
| `release_time_day` | Day of post |
| `release_time_time_of_day` | Time of day (HH:MM:SS) |
| `is_weekend` | Whether posted on weekend |
| `inferred_company_encoded` | Encoded company source |
| `likes` | Target variable |

---

## 📤 Planned API I/O Structure

### 🔹 **Input**
- `Username`
- `Content`
- `Inferred Company`
- `Date and Time Published`
- `Mentions`
- `End of Date (EOD)`

### 🔸 **Output**
- Predicted number of likes by EOD
- Suggestions to increase engagement:
  - Sentiment improvement
  - Use of high-performing keywords
  - Time optimization

---

## 🔮 Future Work

- Model training (Linear Regression, Tree-based models, etc.)
- Model performance evaluation (MAE, R²)
- API deployment using Flask/FastAPI
- Sentiment and keyword optimization modules

---

## 🧾 Deliverables

- ✅ Cleaned dataset
- ✅ Feature-engineered DataFrame
- ✅ EDA plots and insights
- ✅ Planned API structure
- ✅ Feature documentation

---
