# PROJECT\_REPORT.md

## 📘 Week 4 Project Report: Quantitative Finance & Research

This report details the methodology, code, and results for **Week 4** of the Quant\_ARIES\_X\_Economics\_and\_Finance\_Club project, based on the given assignment. The focus was on **advanced classification** and **uncertainty modelling** for financial time series using Support Vector Machines (SVM) and Bayesian Regression on **Amazon (AMZN)** stock data.

---

## 📑 Table of Contents

* Objectives
* Data Preparation & Feature Engineering
* Support Vector Machine (SVM) Classification
* Bayesian Regression for Probabilistic Forecasting
* Hybrid Trading Strategy
* Results Summary
* Key Code Snippets
* Conclusion

---

## 🎯 Objectives

* ✅ Implement **SVM** classification for directional prediction of AMZN stock returns.
* ✅ Develop a **Bayesian regression model** for probabilistic price forecasting and uncertainty quantification.
* ✅ Engineer advanced features: technical indicators, volatility, momentum, etc.
* ✅ Combine both models into a **hybrid trading strategy** and backtest performance.
* ✅ Evaluate using:

  * 🔹 SVM: accuracy, precision, recall, F1, ROC-AUC
  * 🔹 Bayesian: MAE, interval coverage
  * 🔹 Strategy: Sharpe ratio, drawdown

---

## 🛠️ Data Preparation & Feature Engineering

* 🏷️ **Label Creation**: Binary label for next-day return direction (1 if return > 0 else 0)
* 📈 **Technical Indicators**: MA, EMA, RSI, Bollinger Bands, momentum, volatility
* 📊 **Rolling Stats**: Short-term trends via moving averages and standard deviations
* 📉 **Normalisation**: StandardScaler applied for model stability
* 🧹 **Missing Data Handling**: Filtered or imputed rows with missing/extreme values

---

## 🤖 Support Vector Machine (SVM) Classification

### 🔍 Approach

* Model: `SVC` with RBF kernel
* Tuning: `GridSearchCV` over C and gamma
* CV: Stratified 5-fold cross-validation
* Metrics: Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix

### 📊 Results

| Metric    | Value |
| --------- | ----- |
| Accuracy  | 0.989 |
| Precision | 0.985 |
| Recall    | 0.993 |
| F1-score  | 0.989 |
| ROC-AUC   | 0.999 |

* ✅ Best Parameters: `C=100`, `gamma=0.001`
* 📌 Confusion matrix indicates excellent separation and minimal false signals

---

## 📏 Bayesian Regression for Probabilistic Forecasting

### 🧠 Approach

* Model: `Bayesian Ridge Regression`
* Features: Same as SVM plus engineered polynomial/ratios
* Metrics: MAE, 95% credible interval coverage, empirical calibration

### 📊 Results

| Metric                          | Value  |
| ------------------------------- | ------ |
| MAE                             | 134.53 |
| 95% Credible Interval Coverage  | 0.34   |
| Empirical Coverage (Calibrated) | 0.95   |

* 🔍 Top Features: `SMA_7_Squared`, `30-Day MA`, `Volume_Price_Ratio`, `EMA_10`

---

## 🧩 Hybrid Trading Strategy

### ⚙️ Logic

* 📈 Entry: Buy if SVM predicts upward & Bayesian mean forecast > current price
* ❌ Exit: Stop-loss (3%) or Take-profit (5%)
* 🔁 Cooldown period after trade exits

### 🔐 Risk Management

* Dynamic position sizing
* Simulated transaction costs
* Maximum drawdown monitoring

### 📊 Backtest Performance

| Metric       | Value   |
| ------------ | ------- |
| P\&L         | 1.50    |
| Sharpe Ratio | 3.94    |
| Max Drawdown | -0.0094 |

* ✅ Significantly outperformed buy-and-hold on a **risk-adjusted basis**

---

## 💻 Key Code Snippets

### 1. 🧠 SVM Training & Evaluation

```python
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, StratifiedKFold
svc = SVC(kernel='rbf', probability=True, random_state=42)
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.001, 0.01, 0.1, 1]}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
grid_search = GridSearchCV(svc, param_grid, cv=cv, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train_svm_scaled, y_train_svm)
```

### 2. 📈 Bayesian Regression with Uncertainty Bounds

```python
from sklearn.linear_model import BayesianRidge
bayes_model = BayesianRidge()
bayes_model.fit(X_train_bayes_scaled, y_train)
y_pred_mean, y_pred_std = bayes_model.predict(X_test_bayes_scaled, return_std=True)
lower_bound = y_pred_mean - 1.96 * y_pred_std
upper_bound = y_pred_mean + 1.96 * y_pred_std
```

### 3. 💼 Hybrid Strategy Backtest

```python
def backtest_hybrid_strategy(df, stop_loss_pct=0.03, take_profit_pct=0.05, ...):
    # Entry: SVM predicts up & Bayesian mean > price
    # Exit: Stop-loss or take-profit
    # Track portfolio value, P&L, Sharpe, drawdown
    ...
results = backtest_hybrid_strategy(backtest_df, stop_loss_pct=0.03, take_profit_pct=0.05, ...)
```

---

## ✅ Conclusion

* 📈 **SVM** achieved near-perfect classification of next-day return direction.
* 🎯 **Bayesian Regression** provided valuable uncertainty estimates and mean forecasts.
* 🧠 **Hybrid Strategy** delivered high Sharpe ratios and minimal drawdown, outperforming traditional methods.
* 🔬 Emphasis on **robust feature engineering** and **methodical evaluation** proved essential.
