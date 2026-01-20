"""

Objective: Basic data loading and exploration
Tasks
- Load the CSV using Pandas
- Display first 3 rows, column names, and data types
- Create a new column named revenue = units_sold * price

"""

import pandas as pd

df = pd.read_csv('sales_day1.csv')
print("\n--- First 3 Rows ---")
print(df.head(3))

print("\n--- Column Names ---")
print(df.columns)

print("\n--- Data Types ---")
print(df.dtypes)

df['revenue'] = df['units_sold'] * df['price']
print("\nUpdated DataFrame (with Revenue) ---")
print(df.head(3))