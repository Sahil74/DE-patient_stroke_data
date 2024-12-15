from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.providers.google.cloud.operators.datafusion import DataFusionExecutePipelineOperator
from airflow.providers.google.cloud.operators.gcs import GCSFileTransferOperator
from airflow.providers.sftp.hooks.sftp import SFTPHook
from airflow.operators.python import PythonOperator
from datetime import datetime
import kagglehub
import os
from google.cloud import storage

# Function to download dataset from Kaggle A
PI
def download_kaggle_dataset():
    # Download the dataset using kagglehub
    path = kagglehub.dataset_download("fedesoriano/stroke-prediction-dataset")
    print("Dataset downloaded to path:", path)
    return path

# Function to upload data to Google Cloud Storage (GCS)
def upload_to_gcs(local_path, gcs_bucket, gcs_path):
    # Initialize a GCS client
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket)
    
    # Upload the local dataset to GCS
    blob = bucket.blob(gcs_path)
    blob.upload_from_filename(local_path)
    print(f"File uploaded to gs://{gcs_bucket}/{gcs_path}")

# DAG Configuration
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'kaggle_to_bigquery_etl',
    default_args=default_args,
    description='Extract from Kaggle, Transform in DataFusion, and Load to BigQuery',
    schedule_interval=None,  # Set to your preferred schedule
    start_date=datetime(2024, 12, 13),
    catchup=False,
)

# Task 1: Download dataset from Kaggle
download_task = PythonOperator(
    task_id='download_kaggle_dataset',
    python_callable=download_kaggle_dataset,
    dag=dag,
)

# Task 2: Upload dataset to Google Cloud Storage (GCS)
upload_task = PythonOperator(
    task_id='upload_to_gcs',
    python_callable=upload_to_gcs,
    op_args=['/path/to/kaggle/file.csv', 'your-gcs-bucket', 'path/to/dataset/file.csv'],
    dag=dag,
)

# Task 3: Trigger DataFusion Pipeline for Transformation

datafusion_task = DataFusionExecutePipelineOperator(
    task_id="trigger_datafusion_pipeline",
    pipeline_name="your_pipeline_name",  # Replace with your pipeline name
    instance_name="your_datafusion_instance",  # Replace with your Data Fusion instance
    namespace="your_project_id",  # Replace with your GCP project ID
    parameters={"input": "gs://your-gcs-bucket/path/to/dataset/file.csv"},  # Include only necessary parameters
    dag=dag,
)


# Set task dependencies
download_task >> upload_task >> datafusion_task