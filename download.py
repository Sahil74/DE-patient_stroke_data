from datetime import datetime
import os
import kagglehub
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from google.cloud import bigquery

# Download latest version
path = kagglehub.dataset_download("fedesoriano/stroke-prediction-dataset")
print("Path to dataset files:", path)