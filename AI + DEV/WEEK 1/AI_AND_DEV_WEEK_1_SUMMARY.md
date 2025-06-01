
# AI and Dev Week 1 - Dataset Analysis and EDA

## 1. Loading the Dataset
- Loaded a CSV containing 17,331 rows and 7 columns.
- Verified:
  - No missing values.
  - No duplicate entries.
  - Data types for each column.
- Previewed the dataset and extracted column names and uniqueness.

## 2. Light Preprocessing
- Cleaned and standardized text (`content` to lowercase, stripped whitespace).
- Converted `date` to `datetime` format.
- Extracted features like:
  - Year, month, day, time of day
  - Word count and content length
  - Whether it includes media or mentions
  - User post count and average likes per user
  - Weekend flag
- Encoded categorical variables and reorganized columns.

## 3. Exploratory Data Analysis (EDA)
- Plotted distributions and relationships:
  - Likes vs content length, word count, user activity, media presence, etc.
  - Seasonal/monthly trends and company-wise performance
- Used scatter plots, boxplots, histograms, and line charts via Seaborn and Matplotlib.
