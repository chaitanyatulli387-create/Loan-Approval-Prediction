import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/loan_approval_model.pkl")

print("🏦 Loan Approval Prediction")
print("---------------------------")

gender = input("Gender (Male/Female): ").strip().title()

married = input("Married (Yes/No): ").strip().title()

dependents = input("Dependents (0/1/2/3+): ").strip()

education = input(
    "Education (Graduate/Not Graduate): "
).strip().title()

self_employed = input(
    "Self Employed (Yes/No): "
).strip().title()

applicant_income = float(
    input("Applicant Income: ")
)

coapplicant_income = float(
    input("Coapplicant Income: ")
)

loan_amount = float(
    input("Loan Amount: ")
)

loan_term = float(
    input("Loan Amount Term: ")
)

credit_history = float(
    input("Credit History (1 for Good, 0 for Poor): ")
)

property_area = input(
    "Property Area (Urban/Semiurban/Rural): "
).strip().title()


# Create input DataFrame
input_data = pd.DataFrame({
    "Gender": [gender],
    "Married": [married],
    "Dependents": [dependents],
    "Education": [education],
    "Self_Employed": [self_employed],
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [coapplicant_income],
    "LoanAmount": [loan_amount],
    "Loan_Amount_Term": [loan_term],
    "Credit_History": [credit_history],
    "Property_Area": [property_area]
})


# Make prediction
prediction = model.predict(input_data)[0]

probability = (
    model.predict_proba(input_data)[0][1] * 100
)


print("\n🏦 Loan Decision")
print("----------------")

if prediction == 1:
    print("Loan Approval: YES")
else:
    print("Loan Approval: NO")

print(
    "Approval Probability:",
    round(probability, 2),
    "%"
)