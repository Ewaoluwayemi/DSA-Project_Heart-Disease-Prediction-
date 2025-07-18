import streamlit as st
import joblib
import numpy as np

# Load the Random Forest model
model = joblib.load('random_forest_heartdisease_model.pkl')

st.title("Heart Disease Prediction App")
st.write("## By DSA Student")

st.markdown("""
Enter your medical information below to predict whether you're likely to have heart disease.
""")
# Input Fields
# 1. Age
age = st.number_input("Age", min_value=0, step=1)


# 2. Sex
sex = st.selectbox("Sex", options=["Male", "Female"])
sex = 1 if sex == "Male" else 0

# 3. Chest Pain Type
cp_type = st.selectbox(
    "Chest Pain Type",
    options=["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"]
)
cp_map = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}
cp = cp_map[cp_type]

# 4. Resting Blood Pressure
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, step=1)

# 5. Cholesterol
chol = st.number_input("Cholesterol (mg/dL)", min_value=0, step=1)

# 6. Fasting Blood Sugar > 120 mg/dL
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", options=["Yes", "No"])
fbs = 1 if fbs == "Yes" else 0

# 7. Resting ECG
rest_ecg = st.selectbox(
    "Resting ECG Results",
    options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"]
)
ecg_map = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}
restecg = ecg_map[rest_ecg]

# 8. Max Heart Rate Achieved
max_hr = st.number_input("Max Heart Rate Achieved", min_value=0, step=1)

# 9. Exercise Induced Angina
exang = st.selectbox("Exercise Induced Angina", options=["Yes", "No"])
exang = 1 if exang == "Yes" else 0

# 10. Oldpeak (ST depression)
oldpeak = st.number_input("Oldpeak (ST Depression)", min_value=0.0, step=0.1)

# 11. ST Slope
st_slope = st.selectbox("ST Slope", options=["Upsloping", "Flat", "Downsloping"])
slope_map = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}
slope = slope_map[st_slope]

# Combine inputs into a NumPy array
input_features = np.array([[age, sex, cp, resting_bp, chol, fbs, restecg,
                            max_hr, exang, oldpeak, slope]])
                            
# Predict
if st.button("Predict"):
    prediction = model.predict(input_features)
    result = "Likely to Have Heart Disease" if prediction[0] == 1 else "Unlikely to Have Heart Disease"
    st.success(f"Prediction: {result}")