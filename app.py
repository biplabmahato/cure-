import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model_joblib_diabetes')

# Title
st.title("Diabetes Prediction Using Machine Learning")
st.markdown("### Enter the following values:")

# Input fields
p1 = st.number_input("Pregnancies", min_value=0.0)
p2 = st.number_input("Glucose", min_value=0.0)
p3 = st.number_input("Blood Pressure", min_value=0.0)
p4 = st.number_input("Skin Thickness", min_value=0.0)
p5 = st.number_input("Insulin", min_value=0.0)
p6 = st.number_input("BMI", min_value=0.0)
p7 = st.number_input("Diabetes Pedigree Function", min_value=0.0)
p8 = st.number_input("Age", min_value=0.0)

# Predict button
if st.button("Predict"):
    result = model.predict([[p1, p2, p3, p4, p5, p6, p7, p8]])
    if result[0] == 0:
        st.success("Result: Non-Diabetic")
    else:
        st.error("Result: Diabetic")
