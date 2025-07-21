# PROJECT\_REPORT.md

## 📘 Week 2 Project Report: Quantitative Finance & Research

This report presents the pipeline and findings for **Week 2** of the Quant\_ARIES\_X\_Economics\_and\_Finance\_Club project. The week focused on developing predictive models for AMZN stock using machine learning and time-series techniques, supported by feature-rich engineering and backtesting.

---

## 📑 Table of Contents

* Objectives
* Data Overview
* Data Cleaning & Transformation
* Feature Engineering
* Exploratory Analysis
* Model Implementation & Evaluation
* Model Comparison
* Strategy Backtesting
* Conclusion

---

## 🎯 Objectives

* 📊 Prepare a filtered multi-index stock dataset (AAPL, AMZN, GOOGL, MSFT, TSLA)
* 🔍 Analyse price movements and trends using engineered features
* 🧠 Build and evaluate models: Linear Regression, Random Forest, and ARIMA
* 💹 Design a basic trading strategy and assess performance

---

## 📁 Data Overview

* 📚 Source: Kaggle — [US Stock Price Data](https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs)
* 🧱 Structure: MultiIndex DataFrame (Ticker, Date)
* ⏳ Range: Filtered for the **last 10 years** only

---

## 🧹 Data Cleaning & Transformation

* ✅ Dropped duplicate entries and constant column `Open Interest`
* 🧼 Outliers removed using IQR method on 'Close' column
* 🗂️ Filtered for the 5 chosen tickers and the recent decade of data

---

## 🧪 Feature Engineering

Key engineered columns:

* `Daily Return`
* `7-day` and `30-day` Moving Averages
* `30-day` Rolling Volatility
* `Price Change`, `High-Low Spread`, `Intraday Volatility %`
* Lag features: `Lag_1_Daily_Return`, `RSI-14`, `MACD`
* Volume features: `Volume Change`, `Volume/Price Ratio`
* Encoded temporal features: Year, Month, Day, Day of Week, Days since start
* `Close_Log`: Log-transformed close to correct skew

📄 Final dataset exported as `stock_data.csv`

---

## 🔍 Exploratory Analysis

* **Highest Avg Return**: 🏆 `TSLA` → 0.210%
* **Most Volatile Month**: 🌪️ `AMZN` in **Nov 2008** → 6.45%
* 📉 Close price distribution was **right-skewed** (corrected via log transform)
* 📈 Visualisations:

  * Tesla Close vs 30-day MA
  * Amazon Monthly Volatility
  * Correlation matrix with `Close_Log`

---

## 🤖 Model Implementation & Evaluation

### 📍 Target Stock: `AMZN`

* Chronological split: 80% training, 20% testing

### 1. 🔵 **Linear Regression**

* Input: Lagged close prices (5-day history)
* MAE: `0.0140`
* Direction Accuracy: `54.99%`

### 2. 🌲 **Random Forest Regressor**

* Input: Technical indicators (MACD, MA, Volatility, Volume)
* MAE: `0.1631`
* Direction Accuracy: `60.10%`

### 3. 🔁 **ARIMA**

* Auto-configured: `(0,1,0)(0,0,0)[12]`
* MAE: `138.7132`
* Direction Accuracy: `46.76%`

---

## 📊 Model Comparison

| Model             | MAE      | Direction Accuracy |
| ----------------- | -------- | ------------------ |
| Linear Regression | 0.0140   | 54.99%             |
| Random Forest     | 0.1631   | **60.10%**         |
| ARIMA             | 138.7132 | 46.76%             |

✅ **Best MAE:** Linear Regression
✅ **Best Accuracy:** Random Forest

---

## 💹 Strategy Backtesting

Strategy Logic:

* Buy if predicted price > current close
* Else, sell (short)

### 🔁 Simulated Performance:

| Metric            | Value    |
| ----------------- | -------- |
| Strategy Profit   | \$436.99 |
| Buy & Hold Profit | \$339.73 |

📈 Plotted cumulative returns showing the Random Forest strategy outperforming the benchmark.

---

## ✅ Conclusion

* 🧠 Random Forest emerged as the best model based on direction prediction.
* 📉 Linear Regression was surprisingly accurate for log-return prediction.
* 🔁 ARIMA, while informative, underperformed on both fronts.
* 💡 Feature-rich dataset and thorough preprocessing enabled strong modelling.
* 💼 Backtest revealed value of ML-driven strategies over passive investing.

> 🚀 The foundation laid this week supports more advanced strategies and portfolio-level modelling in upcoming phases.

---
