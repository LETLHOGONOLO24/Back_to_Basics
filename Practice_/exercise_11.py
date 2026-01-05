"""

Objective - Clean and prepare time-based data

Tasks
-Load the CSV and convert date to datetime
-Identufy missing values

-Replace missing units_sold with the mean units_sold per category
-Create a revenue column
-Aggregate daily total revenue

"""

import pandas as pd
import datetime

# Lets load the data
df = pd.read_csv('sales_day3.csv')

# Lets convert order_date to datetime
df['date'] = pd.to_datetime(df['date'])

print("\nValues before adding the mean: \n", df['units_sold'])

# Find mean and fill the missing value
mean_value = df['units_sold'].mean()
df['units_sold'] = df['units_sold'].fillna(mean_value)
print("\nThe first 3 rows of the csv file: \n", df.head(7))

# Creating a revenue column
df['revenue'] = df['units_sold'] * df['price']

# Aggregate (sum) daily total revenue
daily_revenue = df.groupby('date')['revenue'].sum().reset_index()
print("\nDaily Total Revenue: \n", daily_revenue)

print("\nLets see the revenue column in action: \n", df.head(7))

df.to_csv('sales_day3_filled.csv', index=False)

