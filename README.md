# 💳 Credit Score Prediction App

A user-friendly Streamlit application that predicts a customer's **credit score** based on financial and personal details. This project demonstrates practical AI/ML skills in the fintech domain and can be a strong addition to your portfolio.

---

## 🚀 Features

- **Manual Input Form:** Enter customer details like age, income, loans, credit card usage, and more.
- **Random Forest Classifier:** Predicts credit score categories (`Good`, `Standard`, `Poor`) accurately.
- **Dynamic Visuals:** Colored score card to highlight the creditworthiness.
- **User-Friendly Interface:** Intuitive layout with clear input sections.
- **Safe Deployment:** Trained model (`credit_model.pkl`) is ignored from the repository for security and size optimization.

---

## 🛠 Technologies Used

- **Python 3.x**
- **Streamlit** – for interactive UI
- **Pandas & NumPy** – for data handling
- **Scikit-learn** – for Random Forest and preprocessing
- **Pickle/Joblib** – to save and load trained model

---

## 📂 Project Structure

CreditScoreApp/
  ├── app.py # Streamlit app
  ├── cred_card.ipynb # Model training notebook
  ├── .gitignore # Ignore models and unnecessary files
  └── README.md


> **Note:** Model file (`credit_model.pkl`) is not included. You need to train the model or place your model file in the project folder before running the app.

---

## ⚡ Installation & Setup

1. Clone the repo:

```bash
git clone https://github.com/pavan656/Credit_score_Prediction.git
cd Credit_score_Prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Place your trained model file (credit_model.pkl) in the project folder.

4. Run the Streamlit app:

```bash
streamlit run app.py
```
## 📈 How to Use

1. Open the app in your browser.
2. Fill in the manual input form with customer financial data.
3. Click Predict Credit Score.
4. View the predicted credit score in a dynamic colored card.

## 🎯 Why This Project Stands Out

1. Focused on fintech and credit scoring – highly relevant for financial services roles.
2. Interactive Streamlit interface makes it user-friendly and portfolio-ready.
3. Can be extended with larger datasets, additional features, or model comparisons.

## 📂 Dataset:

[Credit Score Classification Dataset (Kaggle)](https://www.kaggle.com/datasets/parisrohan/credit-score-classification)

Features include personal details, financials, credit history, and repayment behavior.

## 📌 Future Improvements

1. Add SHAP/LIME explanations to visualize feature impact.
2. Deploy on Streamlit Cloud or Heroku for live access.
3. Integrate with real-world APIs for automated data input.
4. Expand dataset and add hyperparameter tuning for better accuracy.
