❤️ Heart Disease Prediction App
This is a Streamlit-based web application that predicts the likelihood of heart disease using a trained Random Forest Classifier. The model was trained on the heart disease dataset which originated from five different sources.

📁 Project Structure
.
├── app.py                                  # Streamlit web application
├── train_model.py                          # Script to train and save the model
├── random_forest_heartdisease_model.pkl    # Trained Random Forest model
├── requirements.txt                        # Dependencies
└── README.md                               # Project documentation

⚙️ Features
Takes user input for common heart health indicators
Uses a trained Random Forest model to predict heart disease risk
Simple and interactive UI powered by Streamlit
Easy deployment and reproducibility

🚀 How to Run the App
1. Clone the Repository
git clone https://github.com/yourusername/heart-disease-predictor.git
cd heart-disease-predictor

2. (Optional) Create a Virtual Environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

3. Install Required Packages
pip install -r requirements.txt

4. Run the Streamlit App
streamlit run app.py


📦 Requirements
The following Python packages are required (already listed in requirements.txt):
streamlit
joblib
xgboost
numpy
scikit-learn

🧠 Model Details
Model Type: Random Forest Classifier

File: random_forest_heartdisease_model.pkl

Training Script: train_model.py

Input Features: (example: age, sex, cp, resting_bp, chol, fbs, restecg,
                            max_hr, exang, oldpeak, slope)

📝 Notes
The app does not use custom HTML. All UI elements are created using Streamlit components like st.text_input(), st.selectbox(), etc.

🖼️ App Screenshot
![Heart Disease App Screenshot](images/heart-disease-app-screenshot.png)
![Heart Disease App Screenshot](images/heart-disease-app-screenshot.png1)