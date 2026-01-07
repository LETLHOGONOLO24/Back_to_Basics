"""

Objective - Smooth noisy data and identify trends
Tasks
-Load the CSV and convert date to datetime
-Create a revenue column

-Aggregate daily total revenue
-Compute a 3-day rolling average of daily revenue
-Identify days where daily revenue > rolling average

"""

import pandas as pd

# Lets load the data
df = pd.read_csv('sales_day4.csv')

# Lets convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Lets create a revenue column
df['revenue'] = df['units_sold'] * df['price']

# Lets aggregare/sum daily total revenue
daily = df.groupby('date')['revenue'].sum().reset_index()

# Sort by date
daily = daily.sort_values('date')

# 3-day rolling average of daily revenue
daily['3_day_avg'] = daily['revenue'].rolling(3).mean()
print(f"\nLets see the 3-day rolling average: {daily}")