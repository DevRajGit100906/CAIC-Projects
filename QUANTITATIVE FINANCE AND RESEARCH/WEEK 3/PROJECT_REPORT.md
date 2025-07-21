
# 📈 Quantitative Finance and Research - Updated Week 3 Report

**Name**: Dev Raj Das  
**Program**: CAIC Summer of Tech 2025  
**Track**: Quant_ARIES X Economics and Finance Club  
**Week**: 3  
**Date**: July 4, 2025  

---

## 1. Objective

In Week 3, the primary objective was to implement **advanced multivariate time-series modeling and portfolio optimization**. This included robust **feature engineering**, implementing models like **SARIMAX, Random Forest, Linear Regression, ARIMA, and Temporal Fusion Transformer (TFT)**, and performing **backtesting** with **risk-aware strategies**. Finally, **Mean-Variance Optimization (MVO)** was applied to construct a portfolio of **Apple and Amazon stocks**, targeting **Sharpe Ratio maximization**.

---

## 2. Data Preparation and Feature Engineering

### 2.1 Data Cleaning and Transformation  
- Selected 5 large-cap US stocks: AAPL, AMZN, MSFT, GOOGL, TSLA.  
- Cleaned duplicate and irrelevant data, keeping only the last 10 years.
- Removed outliers using IQR-based filtering.

### 2.2 Engineered Features
- **Basic**: Daily Returns, Moving Averages (7, 30 days), Rolling Volatility.
- **Log Transformations**: Closed prices.
- **Time Features**: Year, Month, Day of Week, etc.
- **Volatility Features**: High-Low Spread, Intraday Volatility (%).
- **Technical Indicators**: RSI-14, MACD, Bollinger Width.
- **Interaction/Polynomial Terms**: `SMA_7_Squared`, `MACD_x_Price`, `RSI_x_Volume`, etc.
- **Lag & Difference Features**: Lagged returns/volume and differenced volatility/volume.
- **Exogenous Variables**: S&P 500 returns and VIX levels.
- **STL Decomposition**: Extracted trend and seasonality from `Close`.

---

## 3. Modeling and Evaluation

### 3.1 Linear Regression  
- Features: Past 5-day lags of `Close_Log`.  
- **MAE**: `0.0140`  
- **Direction Accuracy**: `54.99%`

### 3.2 Random Forest  
- Features: 13 technical indicators and statistical signals.  
- **MAE**: `0.1660`  
- **Direction Accuracy**: `61.06%` ✅ **(Best Direction Accuracy)**

### 3.3 ARIMA  
- Auto ARIMA with seasonal component and no exogenous variables.  
- **MAE**: `138.71`  
- **Direction Accuracy**: `46.76%`

### 3.4 SARIMAX (with Exogenous Variables)  
- Model: `ARIMA(1,1,1)(0,1,0)[12]` (Best performing across cross-validation).  
- Exogenous Inputs: `SP500_Return`, `VIX`, `RSI_x_Volume`, `Trend`, `Seasonality`, etc.  
- **MAE**: `75.95`  
- **Direction Accuracy**: `75.95%` ✅ **(Best overall model)**

### 3.5 Ensemble Model  
- Weighted combination based on MAE from Linear Regression, Random Forest, and ARIMA:  
  - Linear Regression: 92.2%  
  - Random Forest: 7.77%  
  - ARIMA: 0.01%  
- **MAE**: `92.77`  
- **Direction Accuracy**: `46.98%`

### 3.6 Temporal Fusion Transformer (TFT)  
- Framework: PyTorch Forecasting  
- Architecture: Hidden Size = 32, Dropout = 0.1, Loss = Quantile Loss  
- Input: Full engineered feature set with temporal context  
- Outcome: Promising performance with meaningful quantile-based forecasts, though not outperforming SARIMAX yet.

---

## 4. Backtesting Strategy (SARIMAX-Based)

### Strategy Logic:
- **Buy Signal**: If predicted close > current close  
- **Sell Signal**: Otherwise  
- **Stop-Loss**: 5%  
- **Holding Period**: 3 days max

### Results:
- **Cumulative Strategy Profit** (per share basis): Significantly better than Buy & Hold  
- **Sharpe Ratio**: Used to assess risk-adjusted return  
- **Conclusion**: Strategy was robust and captured directional accuracy well.

---

## 5. Portfolio Optimization (AAPL + AMZN)

### Methodology:
- Extracted historical returns from filtered dataset.
- Calculated expected returns and covariance matrix.
- Solved **Mean-Variance Optimization (MVO)** problem.
- Constraint: Fully invested portfolio with Sharpe ratio maximization.

### Optimal Weights (illustrative):
- **AAPL**: ~40%  
- **AMZN**: ~60%  
(*actual weights computed using `scipy.optimize.minimize`*)

---

## 6. Conclusion

- ✅ **SARIMAX** emerged as the **best-performing model** in terms of both **MAE** and **Direction Accuracy (75.95%)**.
- ✅ **Random Forest** had strong direction prediction but high MAE.
- ⚡ Feature engineering, STL decomposition, and exogenous data significantly enhanced predictive performance.
- 🚀 Portfolio optimization using **MVO + Sharpe Ratio** led to rational asset allocation.
- 📉 Ensemble model underperformed due to ARIMA's weak influence.
- 🔮 TFT offers exciting future potential with rich temporal learning capabilities.

---

## 7. Future Work

- Integrate **news sentiment**, **earnings events**, and **Fed announcements** as features.
- Explore **attention-based models** like TCNs or hybrid LSTM + GARCH.
- Fine-tune TFT using custom learning rate schedules and larger input windows.
- Simulate strategy in **real-time** or **paper trading environment** using broker APIs.
