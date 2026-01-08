"""

Objective - Quantify relationships
Tasks
-Load the CSV and convert date into datetimr
-Create a revenue column

-Calculate correlation between marketing_spend and units_sold
-Calculate correlation between marketing_spend and revenue
-Interpret which relationship is stronger

"""

import pandas as pd
import datetime

# Lets load the data
df = pd.read_csv('sales_day5.csv')

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Create a revenue column
df['revenue'] = df['units_sold'] * df['price']

# Lets calculate the correlation
corr_spend_units = df['marketing_spend'].corr(df['units_sold'])
corr_spend_revenue = df['marketing_spend'].corr(df['revenue'])

print(f"\nCorrelation (Marketing Spend vs Units Sold): {corr_spend_units:.4f}")
print(f"Correlation (Marketing Spend vs Revenue): {corr_spend_revenue:.4f}")

# Which is stronger?
if abs(corr_spend_units) > abs(corr_spend_revenue):
    print("\nThe relationship between Marketing Spend and Units Sold is stronger.")
else:
    print("\nThe relationship between Marketing Spend and Revenue is stronger.")

"""

In Python, we use the .corr() method from the pandas library to calculate the Pearson Correlation
Coefficient. This number ranges from -1 to +1, where +1 is a perfect positive relationship.

"""
