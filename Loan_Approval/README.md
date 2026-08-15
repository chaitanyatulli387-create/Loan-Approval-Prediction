# 🏦 Loan Approval Prediction

A machine learning project that predicts whether a loan application is likely to be approved based on applicant, financial, credit, and property-related information.

## 📌 Project Overview

This project uses machine learning to analyze loan application details and predict loan eligibility. Users can enter their information through an interactive Streamlit application and receive a loan approval prediction with the estimated approval probability.

## 📊 Features

* Applicant information analysis
* Gender, marital status, and dependents
* Education and employment details
* Applicant and co-applicant income
* Loan amount and loan term
* Credit history
* Property area
* Machine learning based prediction
* Interactive Streamlit interface
* Loan approval probability

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit
* Jupyter Notebook

## 📂 Project Structure

```text
Loan_Approval/
│
├── data/
│   └── Loan_Approval.csv
│
├── models/
│   └── loan_approval_model.pkl
│
├── src/
│   └── predict.py
│
├── app.py
├── Loan_Approval.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 How to Run

Create and activate a virtual environment, then install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application allows the user to enter loan application details and check the predicted loan eligibility.

## 🎯 Output

The application displays:

* **🟢 LOAN APPROVED** or
* **🔴 LOAN NOT APPROVED**

It also displays the estimated approval probability, such as **--.--**.

## ⚠️ Disclaimer

This project is created for educational and demonstration purposes. The prediction should not be considered an actual financial lending decision.
