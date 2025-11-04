import pandas as pd
from sqlalchemy import create_engine

# Read processed data (from previous app.py)
df = pd.read_csv('processed_data.csv')

# Connect to PostgreSQL
engine = create_engine('postgresql://username:password@localhost:5432/mydb')

# Load data into PostgreSQL
df.to_sql('etl_table', engine, if_exists='replace', index=False)

print("ETL pipeline executed successfully!")
