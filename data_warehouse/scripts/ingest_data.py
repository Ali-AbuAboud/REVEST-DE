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

# Load CSV data with error handling for encoding
csv_path = r"D:\Ali\REVEST\data_warehouse\data\Sales.csv"
df = pd.read_csv(csv_path, encoding='utf-8', on_bad_lines='skip')  # Using on_bad_lines='skip' instead of error_bad_lines

# Remove problematic characters (non-breaking spaces and other strange characters)
df.replace({r'\xc2\xa0': ' '}, regex=True, inplace=True)

# Rename columns to match PostgreSQL table
column_mapping = {
    'Row ID': 'row_id',
    'Order ID': 'order_id',
    'Order Date': 'order_date',
    'Ship Date': 'ship_date',
    'Ship Mode': 'ship_mode',
    'Customer ID': 'customer_id',
    'Customer Name': 'customer_name',
    'Segment': 'segment',
    'Country': 'country',
    'City': 'city',
    'State': 'state',
    'Postal Code': 'postal_code',
    'Region': 'region',
    'Product ID': 'product_id',
    'Category': 'category',
    'Sub-Category': 'sub_category',
    'Product Name': 'product_name',
    'Sales': 'sales'
}
df.rename(columns=column_mapping, inplace=True)

# Ensure correct data types
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')

# Drop 'row_id' column for insertion (let PostgreSQL handle it)
df.drop(columns=['row_id'], inplace=True)

# Ingest data into PostgreSQL
df.to_sql('sales', engine, if_exists='append', index=False)

print("Data ingestion completed successfully.")
