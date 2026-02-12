import pandas as pd
from sqlalchemy import create_engine

# 1. Load the data
file_path = r'C:\Users\HLOGIZNBUCKS\Downloads\Back_to_Basics\Data_Science\Week_3\sales.csv'
df = pd.read_csv(file_path)

# 2. Connect to Postgres
# Format: 'postgresql://username:password@localhost:5432/database_name'
engine = create_engine('postgresql://postgres:Menjukapoy123@localhost:5432/PostgreSQL_18')

# 3. Upload
# if_exists='append' adds to existing table; 'replace' creates a new one
df.to_sql('sales_table', engine, if_exists='append', index=False)

print("Data uploaded successfully!")