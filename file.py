import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def transform_data(element):
    # Assuming 'element' is a dictionary with columns in the dataset

    # Handle missing values
    element['bmi'] = element.get('bmi', None) or 25.0  # Example of handling missing BMI
    numerical_columns = ['age', 'hypertension', 'heart_disease', 'avg_glucose_level']
    for column in numerical_columns:
        element[column] = element.get(column, None) or 0  # Handle missing numerical values

    # Encode categorical variables (simplified example for demo)
    categorical_columns = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
    le = LabelEncoder()
    for column in categorical_columns:
        element[column] = le.fit_transform([element[column]])[0]  # Encoding categorical variable

    # Outlier detection & capping (simplified example, adjust as needed)
    Q1 = element['age'] - 1.5 * element['age']
    Q3 = element['age'] + 1.5 * element['age']
    element['age'] = min(max(element['age'], Q1), Q3)

    # Normalize/scale numerical features
    scaler = StandardScaler()
    element[numerical_columns] = scaler.fit_transform([element[numerical_columns]])[0]

    return element
