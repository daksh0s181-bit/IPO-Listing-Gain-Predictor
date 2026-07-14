# app.py - IPO Listing Gain Predictor

import streamlit as st
import pickle
import numpy as np
import os

# Load model and scaler
base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'ipo_model.pkl'), 'rb') as f:
    model = pickle.load(f)

with open(os.path.join(base_dir, 'ipo_scaler.pkl'), 'rb') as f:
    scaler = pickle.load(f)

# Sidebar
st.sidebar.title('ℹ️ About')
st.sidebar.write('This app predicts IPO listing day gain % based on subscription data.')
st.sidebar.write('**Model:** Linear Regression')
st.sidebar.write('**R² Score:** 0.54')
st.sidebar.write('**Dataset:** 648 Indian IPOs')
st.sidebar.warning('⚠️ For educational purposes only — not financial advice!')

import streamlit as st
import base64

def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background(r"D:\code\proj\IPO model\money2.png")



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