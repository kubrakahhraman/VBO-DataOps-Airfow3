import pandas as pd
from sqlalchemy import create_engine

# Path to the raw data in RustFS
file_path = "/dataops/raw/dirty_store_transactions.csv"

# Load and clean the data
df = pd.read_csv(file_path)
df = df.drop_duplicates()
df = df.fillna(method='ffill')

# Write the cleaned data to the PostgreSQL database
engine = create_engine('postgresql://airflow:airflow@postgres:5432/traindb')
df.to_sql('clean_data_transactions', engine, if_exists='replace', index=False)