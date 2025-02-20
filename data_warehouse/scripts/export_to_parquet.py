import pandas as pd
from sqlalchemy import create_engine

# Database connection settings
DB_USER = 'postgres'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'revest'

# Create database engine
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Load data from PostgreSQL into DataFrame
df = pd.read_sql('SELECT * FROM sales', engine)

# Export DataFrame to Parquet file
df.to_parquet('sales_data.parquet')

print("Data exported to Parquet file successfully.")
