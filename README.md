# 📈 IPO Listing Gain Predictor

## 🎯 Objective
Predict the expected listing day gain % of an Indian IPO based on 
subscription data — helping investors make data-driven decisions 
before applying for an IPO.

---

## 🚀 Live Demo
https://ipo-listing-gain-predictor-6udpy3wh6gmypnqfppmv8o.streamlit.app/

---

## 📊 Key Findings

🔸 **68.5% of Indian IPOs list positive** on day 1 — but the average 
   gain of 16.5% is misleading. Most IPOs list between -10% to +20%.

🔸 **Total subscription rate (0.71 correlation)** is the strongest 
   predictor of listing gain — followed by HNI (0.62) and QIB (0.60).

🔸 **Sigachi Industries** holds the record — 253% listing gain. 
   Om Freight Forwarders was the worst at -39%.

🔸 **Offer price has almost zero impact (0.03)** on listing gain — 
   cheap vs expensive IPOs perform similarly.

---

## 🤖 ML Model

| Model | R² Score | MAE |
|-------|----------|-----|
| Linear Regression | **0.54** ✅ | 12.5% |
| Random Forest | 0.45 | 13.7% |
| XGBoost | 0.53 | 12.8% |

**Best Model:** Linear Regression
**Prediction Error:** ±12% on average

---

## 🛠️ Tech Stack

- **Python** — Core language
- **Pandas** — Data cleaning & analysis
- **Matplotlib / Seaborn** — Visualizations
- **Scikit-learn** — ML model
- **Streamlit** — Web app

---

## 📦 Requirements
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
xgboost
openpyxl

---

## ⚠️ Disclaimer
This project is for **educational purposes only** — not financial advice.
IPO investments carry real risk. Always consult a SEBI registered 
advisor before investing.
