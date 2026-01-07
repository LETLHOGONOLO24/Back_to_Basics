"""

Objective - Understand how spread matters, not just averages
Tasks
-Extract units_sold as a NumPy array

-Calculate variance and standard deviation
-Identify which transactions are more than 1 standard deviation above the mean

"""

import numpy as np
import pandas as pd

# Lets load the data pandas style
df = pd.read_csv('sales_day4.csv')

# Extract units_sold as a NumPy array
arr = np.array(df['units_sold'])
print(f"\nUnits_sold as an array: {arr}")

# Lets calculate revenue first
df['revenue'] = df['units_sold'] * df['price']

# Lets calculate variance and standard deviation
variance = df['revenue'].var()
std_dev = df['revenue'].std()
mean_revenue = df['revenue'].mean()

print(f"\nVariance: {variance:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Mean Revenue: R{mean_revenue:.2f}")

# Lets calculate threshold
threshold = mean_revenue + std_dev

# Lets find high transactions
high_transactions = df[df['revenue'] > threshold]

print(f"\nThreshold (Mean + 1 STD): R{threshold:.2f}")
print(f"\nTransactions above threshold:")
print(high_transactions[['date', 'product', 'revenue']])