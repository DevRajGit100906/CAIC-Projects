# PROJECT\_REPORT.md

## 📘 Week 1 Project Report: Quantitative Finance & Research

This report outlines the process and findings for **Week 1** of the Quant\_ARIES\_X\_Economics\_and\_Finance\_Club track. The focus was on building a clean, multi-ticker historical stock dataset, engineering essential time-series features, and performing basic exploratory analysis using stock data from **Apple (AAPL), Amazon (AMZN), Google (GOOGL), Microsoft (MSFT), and Tesla (TSLA)**.

---

## 📑 Table of Contents

* Objectives
* Data Access
* Data Cleaning
* Data Transformation
* Exploratory Analysis
* Visualizations
* Conclusion

---

## 🎯 Objectives

* 📥 Access price-volume data for selected large-cap US stocks.
* 🧹 Clean and organize the data using MultiIndex format.
* ⚙️ Create key time-series features (returns, moving averages, volatility).
* 📊 Perform basic exploratory analytics to identify standout stocks.
* 📈 Visualize core trends and volatility over time.

---

## 💾 Data Access

* 📚 Source: [Kaggle Dataset – US Stocks](https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs)
* ✅ Stocks selected: AAPL, AMZN, GOOGL, MSFT, TSLA
* 🏷️ Data Structure: MultiIndex DataFrame (Ticker, Date)
* 📅 Date range converted to `datetime` format and sorted in descending order

```python
multiindex_df = combined_df.set_index(['Ticker', 'Date']).sort_index(ascending=False)
```

---

## 🧹 Data Cleaning

* Checked for missing values ➝ **None found** ✅
* Identified and removed 6 duplicate rows outside relevant date range
* Dropped constant column `Open Interest`
* Filtered dataset to last 10 years for relevance
* Validated consistent data types across all columns

📊 Final dimensions: **26,685 rows × 5 columns**

```python
multiindex_df.drop_duplicates(inplace=True)
multiindex_df = multiindex_df.drop(columns=['Open Interest'])
```

---

## 🔁 Data Transformation

For each stock, added the following engineered features:

* 📉 **Daily Return**: % change in close price
* 📈 **7-Day Moving Average** (MA)
* 📉 **30-Day Moving Average** (MA)
* 📉 **30-Day Rolling Volatility**: Std deviation of daily returns

```python
filtered_df_sorted['Daily Return'] = filtered_df_sorted.groupby('Ticker')['Close'].pct_change() * 100
filtered_df_sorted['7-Day Moving Average'] = ...
filtered_df_sorted['30-Day Moving Average'] = ...
filtered_df_sorted['Rolling Volatility (30d)'] = ...
```

---

## 🔍 Exploratory Analysis

### ✅ Q1: Stock with Highest Average Return

| Ticker   | Avg Return (%) |
| -------- | -------------- |
| AAPL     | 0.106          |
| AMZN     | 0.136          |
| GOOGL    | 0.064          |
| MSFT     | 0.059          |
| **TSLA** | **0.210**      |

📌 **Winner:** TSLA had the highest average return over the 10-year period.

---

### ✅ Q2: Stock with Most Volatile Month

* 📆 **Month:** November 2008
* 📈 **Stock:** AMZN
* 📊 **Rolling Volatility:** 6.45%
* 📈 **Avg Volatility Across Stocks:** 5.72%

```python
monthly_volatility = volatility_unstacked.resample('M').mean()
most_volatile_stock_in_month = monthly_volatility.loc[max_month].idxmax()
```

---

## 📊 Data Visualizations

### 1. 📉 Tesla – Close Price vs. 30-Day Moving Average

```python
tsla_data = filtered_df_sorted.loc['tsla']
tsla_data.plot(y=['Close', '30-Day Moving Average'], figsize=(12, 6))
plt.title('Tesla: Price vs. 30-Day Moving Average')
```

### 2. 📉 Amazon – Monthly Rolling Volatility

```python
amzn_monthly_volatility.plot(kind='bar')
plt.title('Amazon Monthly Rolling Volatility (30d)')
```

---

## ✅ Conclusion

* 🧹 Cleaned and structured data for 5 major US stocks over 10 years
* 📈 Engineered meaningful financial features to assess trends and risk
* 🔍 Identified **TSLA** as top performer in terms of return
* ⚠️ Identified **AMZN** as most volatile during 2008 financial crisis
* 📊 Visualizations highlighted long-term performance and volatility patterns

> 🚀 This foundational work sets up the pipeline for more advanced modeling and strategy building in future weeks.

---
