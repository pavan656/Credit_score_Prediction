import streamlit as st
import pandas as pd
import joblib

# ---------------------------
# Page Config — must be first
# ---------------------------
st.set_page_config(page_title="Credit Score Predictor", layout="centered")

# ---------------------------
# Load Model & Encoders
# ---------------------------
@st.cache_resource
def load_model():
    model, encoders, target_encoder, feature_cols = joblib.load("credit_model.pkl")
    return model, encoders, target_encoder, feature_cols

model, encoders, target_encoder, feature_cols = load_model()

# ---------------------------
# App Layout
# ---------------------------
st.title("💳 Credit Score Prediction App")
st.write("Fill in the details below to predict your credit score")

# ---------------------------
# Manual Entry Form
# ---------------------------
with st.form("credit_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 30)
        income = st.number_input("Annual Income (₹)", 0, 5000000, 500000, step=10000)
        salary = st.number_input("Monthly Salary (₹)", 0, 500000, 40000, step=1000)
        accounts = st.number_input("Number of Bank Accounts", 0, 20, 2)
        credit_cards = st.number_input("Number of Credit Cards", 0, 20, 3)
        interest_rate = st.number_input("Interest Rate (%)", 0, 100, 10)

    with col2:
        loans = st.number_input("Number of Loans", 0, 20, 1)
        delay_days = st.number_input("Delay from Due Date (days)", 0, 365, 5)
        delayed_payments = st.number_input("Number of Delayed Payments", 0, 100, 2)
        debt = st.number_input("Outstanding Debt (₹)", 0, 10000000, 100000, step=10000)
        utilization = st.slider("Credit Utilization Ratio", 0.0, 1.0, 0.3)
        emi = st.number_input("Total EMI per Month (₹)", 0, 1000000, 20000, step=1000)

    submitted = st.form_submit_button("🔮 Predict Credit Score")

# ---------------------------
# Prediction
# ---------------------------
if submitted:
    input_data = {
        "Age": age,
        "Annual_Income": income,
        "Monthly_Inhand_Salary": salary,
        "Num_Bank_Accounts": accounts,
        "Num_Credit_Card": credit_cards,
        "Interest_Rate": interest_rate,
        "Num_of_Loan": loans,
        "Delay_from_due_date": delay_days,
        "Num_of_Delayed_Payment": delayed_payments,
        "Outstanding_Debt": debt,
        "Credit_Utilization_Ratio": utilization,
        "Total_EMI_per_month": emi,
    }
    df_input = pd.DataFrame([input_data])

    # Add missing features with default 0
    for col in feature_cols:
        if col not in df_input.columns:
            df_input[col] = 0
    df_input = df_input[feature_cols]

    # Encode categorical fields safely
    for col, le in encoders.items():
        if col in df_input.columns:
            df_input[col] = df_input[col].astype(str).apply(
                lambda x: x if x in le.classes_ else le.classes_[0]
            )
            df_input[col] = le.transform(df_input[col])


    # Predict
    pred = model.predict(df_input)[0]
    score = target_encoder.inverse_transform([pred])[0]

    # Color & emoji
    if score.lower() == "good":
        color = "#2ecc71"
        emoji = "✅"
    elif score.lower() == "standard":
        color = "#f39c12"
        emoji = "⚠️"
    else:
        color = "#e74c3c"
        emoji = "❌"

    st.markdown(
        f"""
        <div style="
            background-color:#f0f8ff;
            padding:30px;
            border-radius:15px;
            text-align:center;
            box-shadow:2px 2px 15px rgba(0,0,0,0.2);
        ">
            <h2 style="color:#34495e;">🎯 Predicted Credit Score</h2>
            <h1 style="font-size:50px; color:{color};">{score} {emoji}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
