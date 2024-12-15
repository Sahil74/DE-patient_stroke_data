# Stroke Prediction Data Engineering Project

## Project Overview
This project focuses on building an end-to-end data engineering pipeline for the **Stroke Prediction Dataset**, which contains clinical data used to predict the likelihood of stroke events. The dataset includes 11 clinical features such as age, gender, hypertension, heart disease, and smoking status. By leveraging tools like Google Cloud Platform (GCP) and Looker Studio, this project automates the ingestion, transformation, and visualization of data to enable actionable insights for healthcare professionals.

---

## Dataset Information

### **Dataset Overview**
The dataset is designed to predict whether a patient is likely to have a stroke based on various clinical features. According to the World Health Organization (WHO), stroke is the second leading cause of death globally, accounting for approximately 11% of total deaths. This dataset aims to aid predictive analysis in healthcare by providing relevant patient information.

### **Attribute Information**
- **id**: Unique identifier for each patient.
- **gender**: Patient's gender ("Male", "Female", or "Other").
- **age**: Patient's age.
- **hypertension**: 1 if the patient has hypertension; 0 otherwise.
- **heart_disease**: 1 if the patient has heart disease; 0 otherwise.
- **ever_married**: Whether the patient has ever been married ("Yes" or "No").
- **work_type**: Patient's type of work ("children", "Govt_job", "Never_worked", "Private", or "Self-employed").
- **Residence_type**: Patient's residence type ("Rural" or "Urban").
- **avg_glucose_level**: Average glucose level in the blood.
- **bmi**: Body mass index.
- **smoking_status**: Smoking status ("formerly smoked", "never smoked", "smokes", or "Unknown").
- **stroke**: 1 if the patient had a stroke; 0 otherwise.

*Note*: "Unknown" in smoking status indicates unavailable information for that patient.

---

## Data Engineering Pipeline

The project uses a combination of GCP tools and technologies to process and analyze the dataset efficiently:

1. **Data Ingestion**:
   - A **DAG (Directed Acyclic Graph)** implemented in `dag.py` downloads the dataset from Kaggle and stores it in a **Google Cloud Storage (GCS)** bucket.

2. **Data Transformation**:
   - The ingestion process triggers a **Google Cloud Data Fusion** pipeline.
   - The pipeline performs **Extract, Transform, and Load (ETL)** tasks, such as cleaning missing values, encoding categorical variables, and normalizing numerical features.

3. **Data Loading**:
   - The transformed data is loaded into **BigQuery**, a fully-managed data warehouse for large-scale query processing.

4. **Data Visualization**:
   - The processed data is visualized using **Looker Studio** (formerly Google Data Studio), with interactive dashboards highlighting key metrics and patterns in stroke predictions.

---

## Findings

### Key Insights from the Analysis:
- **Age and Stroke Incidence**:
  - Patients aged 60 and above showed a significantly higher likelihood of stroke, emphasizing the importance of early intervention and regular health monitoring in older populations.

- **Impact of Hypertension and Heart Disease**:
  - Over 70% of stroke cases were associated with patients who had either hypertension, heart disease, or both.

- **Smoking Status**:
  - Smokers, particularly those with pre-existing conditions, demonstrated a higher risk of stroke compared to non-smokers.

- **BMI and Glucose Levels**:
  - High BMI and elevated average glucose levels correlated strongly with stroke events, highlighting the need for lifestyle modifications to mitigate risks.

---

## Tools and Technologies Used
- **Languages**: Python
- **Orchestration**: Apache Airflow (via `dag.py`)
- **Cloud Platform**: Google Cloud Platform (GCP)
  - **Google Cloud Storage (GCS)**
  - **BigQuery**
  - **Google Cloud Data Fusion**
- **Visualization**: Looker Studio


---

## Conclusion

This project demonstrates how modern data engineering practices can be applied to healthcare datasets to derive valuable insights. By automating the data pipeline, healthcare professionals can focus on decision-making rather than data processing, potentially improving patient outcomes in stroke prevention and management.
