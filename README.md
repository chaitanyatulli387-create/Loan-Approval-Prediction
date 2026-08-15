# Loan Approval Prediction

A machine learning project that predicts whether a loan application is likely to be approved.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Flask
* Joblib
* Jupyter Notebook

## Dataset

Loan Approval Prediction dataset.

The dataset contains information about loan applicants, including their income, education, employment status, credit history, loan amount, loan term, and property area.

## Machine Learning Models

The project compares:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. K-Nearest Neighbors

Models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score

The model with the highest F1 score is selected as the final model.

## Project Structure

```text
Loan-Approval-Prediction/
│
├── data/
│   └── loan_data.csv
│
├── models/
│   ├── loan_approval_model.pkl
│   └── model_comparison.csv
│
├── src/
│   └── train_model.py
│
├── Loan_Approval_Prediction.ipynb
├── app.py
├── requirements.txt
└── README.md
