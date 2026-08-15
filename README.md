# Employee Salary Prediction

A machine learning project that predicts an employee's salary based on factors such as experience, education, job role, and other relevant features.

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

Employee Salary Prediction dataset.

The dataset contains information about employees, including their years of experience, education level, job title, age, and other relevant details used to predict salary.

## Machine Learning Models

The project compares:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. K-Nearest Neighbors Regressor

Models are evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

The model with the best performance is selected as the final model.

## Project Structure

```text
Employee-Salary-Prediction/
│
├── data/
│   └── salary_data.csv
│
├── models/
│   ├── salary_model.pkl
│   └── model_comparison.csv
│
├── src/
│   └── train_model.py
│
├── Employee_Salary_Prediction.ipynb
├── app.py
├── requirements.txt
└── README.md
