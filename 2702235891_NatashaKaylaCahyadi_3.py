import streamlit as st
import requests

st.set_page_config(page_title="Obesity Prediction", layout="centered")

st.title("🧠 Obesity Prediction App")
st.markdown("Please fill in your lifestyle and health-related data below:")

with st.form("obesity_form"):
    Gender = st.radio("Gender", ['Male', 'Female'])
    Age = int(st.number_input("Age", min_value=1, max_value=120, step=1))
    Height = st.number_input("Height (meters)", min_value=0.5, max_value=2.5, format="%.2f")
    Weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, format="%.1f")
    family_history_with_overweight = st.radio("Family History with Overweight?", ['yes', 'no'])
    FAVC = st.radio("Do you frequently consume high-calorie food (FAVC)?", ['yes', 'no'])
    FCVC = st.slider("Frequency of vegetable consumption (FCVC)", 0.0, 3.0, step=0.01)
    NCP = st.slider("Number of main meals per day (NCP)", 1.0, 4.0, step=0.01)
    CAEC = st.selectbox("Do you eat between meals (CAEC)?", ['Always', 'Frequently', 'Sometimes', 'no'])
    SMOKE = st.radio("Do you smoke?", ['yes', 'no'])
    CH2O = st.slider("Water consumption (liters/day) (CH2O)", 0.0, 3.0, step=0.01)
    SCC = st.radio("Do you monitor your calorie intake (SCC)?", ['yes', 'no'])
    FAF = st.slider("Physical activity (hours/week) (FAF)", 0.0, 3.0, step=0.01)
    TUE = st.slider("Daily technology usage (hours/day) (TUE)", 0.0, 3.0, step=0.01)
    CALC = st.selectbox("Alcohol consumption (CALC)", ['Frequently', 'Sometimes', 'no'])
    MTRANS = st.selectbox("Transportation type (MTRANS)", ['Automobile', 'Bike', 'Motorbike', 'Public_Transportation', 'Walking'])

    submitted = st.form_submit_button("Predict")

if submitted:
    API_URL = "http://127.0.0.1:8000/predict"  

    input_data = {
        "Gender": Gender,
        "Age": Age,
        "Height": Height,
        "Weight": Weight,
        "family_history_with_overweight": family_history_with_overweight,
        "FAVC": FAVC,
        "FCVC": FCVC,
        "NCP": NCP,
        "CAEC": CAEC,
        "SMOKE": SMOKE,
        "CH2O": CH2O,
        "SCC": SCC,
        "FAF": FAF,
        "TUE": TUE,
        "CALC": CALC,
        "MTRANS": MTRANS
    }

    with st.spinner("Predicting..."):
        try:
            response = requests.post(API_URL, json=input_data)
            if response.status_code == 200:
                result = response.json()
                st.success(f"🎯 **Predicted Obesity Category:** `{result['Prediction']}`")
            else:
                st.error(f"❌ Prediction failed: {response.status_code}")
        except Exception as e:
            st.error(f"⚠️ Error connecting to FastAPI server: {e}")
