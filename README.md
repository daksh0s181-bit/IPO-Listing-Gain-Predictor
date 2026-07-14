# 📈 IPO Listing Gain Predictor

## 🎯 Objective
Predict the expected listing day gain % of an Indian IPO based on 
subscription data — helping investors make data-driven decisions 
before applying for an IPO.

---

## 🚀 Live Demo


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

## 📁 Project StructureLength*: 114,086 tokens | Cost: $0.04 | Cached for: 56mClaude finished the responseyup lets proceed🟡 Step — Save the Best Model
python# Save Best Model (Linear Regression)

import pickle
import os

os.makedirs('model', exist_ok=True)

# Save model
with open('model/ipo_model.pkl', 'wb') as f:
    pickle.dump(lr2, f)

# Save scaler
with open('model/ipo_scaler.pkl', 'wb') as f:
    pickle.dump(scaler2, f)

print("✅ Model saved!")
print("✅ Scaler saved!")

▶️ Run and tell me output — then we build the Streamlit app! 🚀MODEL SAVED SCALER SAVEDLet's build the Streamlit app now! 🔥
Create a new file app.py in your project folder and paste this:
python# app.py - IPO Listing Gain Predictor

import streamlit as st
import pickle
import numpy as np
import os

# Load model and scaler
base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'model/ipo_model.pkl'), 'rb') as f:
    model = pickle.load(f)

with open(os.path.join(base_dir, 'model/ipo_scaler.pkl'), 'rb') as f:
    scaler = pickle.load(f)

# Sidebar
st.sidebar.title('ℹ️ About')
st.sidebar.write('This app predicts IPO listing day gain % based on subscription data.')
st.sidebar.write('**Model:** Linear Regression')
st.sidebar.write('**R² Score:** 0.54')
st.sidebar.write('**Dataset:** 648 Indian IPOs')
st.sidebar.warning('⚠️ For educational purposes only — not financial advice!')

# App title
st.title('📈 IPO Listing Gain Predictor')
st.write('Enter IPO details below to predict expected listing day gain')

# Input fields
col1, col2 = st.columns(2)

with col1:
    issue_size = st.number_input('Issue Size (Crores)', min_value=0.0, max_value=50000.0, value=500.0)
    qib = st.number_input('QIB Subscription (times)', min_value=0.0, max_value=500.0, value=10.0)
    hni = st.number_input('HNI Subscription (times)', min_value=0.0, max_value=500.0, value=10.0)

with col2:
    rii = st.number_input('RII Subscription (times)', min_value=0.0, max_value=500.0, value=10.0)
    total = st.number_input('Total Subscription (times)', min_value=0.0, max_value=500.0, value=10.0)
    offer_price = st.number_input('Offer Price (₹)', min_value=0.0, max_value=5000.0, value=200.0)

# Predict button
if st.button('🔍 Predict Listing Gain'):

    # Create input array
    input_data = np.array([[issue_size, qib, hni, rii, total, offer_price]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]

    # Show result
    st.divider()

    if prediction > 20:
        st.success(f'📈 Expected Listing Gain: +{prediction:.1f}%')
        st.write('🟢 **Investment Signal: Strong IPO — Good chance of positive listing**')
    elif prediction > 0:
        st.info(f'📊 Expected Listing Gain: +{prediction:.1f}%')
        st.write('🟡 **Investment Signal: Average IPO — Moderate listing expected**')
    else:
        st.error(f'📉 Expected Listing Gain: {prediction:.1f}%')
        st.write('🔴 **Investment Signal: Weak IPO — Possible listing at discount**')

    st.progress(min(int(abs(prediction)), 100))
    st.caption(f'Model confidence based on R² = 0.54 — predictions may vary by ±12%')

Run the app:
streamlit run "your path\app.py"

📌 What's different from liver disease app:
FeaturePurpose3 color coded resultsGreen/Yellow/Red based on predictionst.progress()Visual bar showing gain magnitude±12% captionHonest about model limitationsInvestment signalBusiness insight not just a number

▶️ Run and share a screenshot! 🚀excerpt_from_previous_claude_message.txt1 linetxthow can i change background to an imageTo add a background image in Streamlit, add this function at the top of your app, right after the imports:
pythonimport base64

def set_background(image_path):
    with open(image_path, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call it right after imports
set_background('background.jpg')  # put your image name here

📌 What this does & why:
LinePurposeopen(image_path, 'rb')Opens image in binary modebase64.b64encode()Converts image to base64 string — browser can read it directlyst.markdown(css)Injects custom CSS into Streamlitbackground-size: coverImage covers entire screenbackground-attachment: fixedImage stays fixed while scrolling

Steps:

Save any image as background.jpg in your project folder
Add this code to your app.py
Call set_background('background.jpg') after imports


▶️ Try it and share the screenshot! 🚀i wanna upload this project on github so write a readme sectionHere's your complete README:
markdown# 📈 IPO Listing Gain Predictor

## 🎯 Objective
Predict the expected listing day gain % of an Indian IPO based on 
subscription data — helping investors make data-driven decisions 
before applying for an IPO.

---

## 🚀 Live Demo
[Click here to try the app](#) ← add your Streamlit Cloud link here

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
