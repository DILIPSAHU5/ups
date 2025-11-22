import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("titanic.pkl")
# scaler = joblib.load("st_ups.pkl")

# Prediction function
def predict_price(Pclass, Age, SibSp, Parch, Fare, Gender):
    input_data = pd.DataFrame([[Pclass, Age, SibSp, Parch, Fare, Gender]],
                              columns=['Pclass','Age','SibSp','Parch','Fare','Gender'])
    prediction = model.predict(input_data)
    return "Survived 🟩" if prediction[0] == 1 else "Not Survived 🟥"

# ---------- Page Config ----------
st.set_page_config(
    page_title="Titanic Survival Prediction App",
    page_icon="🚢",
    layout="wide",
)

# ---------- Custom CSS ----------
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
background: linear-gradient(to bottom right, #0f4c75, #3282b8, #bbe1fa);
}
[data-testid="stHeader"] {background-color: rgba(0,0,0,0);}
h1 {color: #ffffff !important;}
label {font-weight: 600 !important;}
div.stButton > button {
    background-color: #1b262c;
    color: white;
    border-radius: 8px;
    font-size: 20px;
    padding: 0.5rem 1.2rem;
}
div.stButton > button:hover {
    background-color: #0f4c75;
    color: #ffffff;
    transform: scale(1.05);
}
.result-card {
    padding: 15px;
    text-align: center;
    border-radius: 12px;
    font-size: 24px;
    font-weight: 700;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------- Title ----------
st.markdown("<h1 style='text-align: center;'>🚢 Titanic Survival Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px; color:white;'>Enter passenger details to predict survival probability</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)

# ---------- Input Form ----------
col1, col2 = st.columns(2)

with col1:
    Pclass = st.selectbox("🎟 Passenger Class (1=Upper, 2=Middle, 3=Lower)", [1, 2, 3])
    Age = st.number_input("🎂 Age", min_value=0, max_value=100, value=30)

    # ---- Converted to Radio Button ----
    SibSp = st.radio("👫 Siblings/Spouse with you? (0 = No, 1 = Yes)", [0, 1], horizontal=True)

with col2:
    # ---- Converted to Radio Button ----
    Parch = st.radio("👨‍👩‍👧 Parents/Children with you? (0 = No, 1 = Yes)", [0, 1], horizontal=True)

    Fare = st.number_input("💰 Fare (Ticket Price)", min_value=0.0, value=30.0)
    Gender = st.radio("⚧ Gender (0 = Female, 1 = Male)", [0, 1], horizontal=True)

# ---------- Buttons ----------
colA, colB, colC = st.columns([1,1,1])

predict_btn = colA.button("🔮 Predict")
reset_btn = colC.button("♻ Reset")

# ---------- Prediction ----------
if predict_btn:
    result = predict_price(Pclass, Age, SibSp, Parch, Fare, Gender)
    color = "#4CAF50" if "Survived" in result else "#f44336"
    
    st.markdown(
        f"<div class='result-card' style='background-color:{color}; color:white;'>{result}</div>",
        unsafe_allow_html=True
    )

if reset_btn:
    st.experimental_rerun()
