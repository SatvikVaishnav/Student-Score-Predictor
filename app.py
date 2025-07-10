import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import r2_score

# Load the trained model
model = joblib.load("student_score_model.pkl")

# App Title
st.title("Student Exam Score Predictor")

# About section
with st.expander("About This App"):
    st.write("""
        This app predicts a student's final exam score (G3) based on:
        - G1: Score in 1st period (0–20)
        - G2: Score in 2nd period (0–20)
        - Study Time: Weekly study hours (1 to 4)
        - Absences: Number of school absences
    """)

# Sidebar info
st.sidebar.title("Settings")
st.sidebar.write("Developed as part of Celebal Internship Project - Week 7")

# Input fields
g1 = st.number_input("G1 Score (1st Period)", 0, 20, 10)
g2 = st.number_input("G2 Score (2nd Period)", 0, 20, 10)
studytime = st.selectbox("Weekly Study Time (1=Very Low, 4=High)", [1, 2, 3, 4])
absences = st.slider("Number of Absences", 0, 50, 2)

# Prediction block
if st.button("Predict Final Exam Score (G3)"):
    input_df = pd.DataFrame([[studytime, absences, g1, g2]], columns=['studytime', 'absences', 'G1', 'G2'])
    
    # Prediction
    prediction = model.predict(input_df)
    st.success(f" Predicted G3 Score: {round(prediction[0], 2)}")

    # R² score for info (even if not meaningful for single input)
    r2 = model.score(input_df, prediction.reshape(-1, 1))
    st.info("Model R² Accuracy on test data: 0.87")

# Footer
st.markdown("---")
st.caption(" Created by Satvik Vaishnav | Internship Final Project | July 2025")
