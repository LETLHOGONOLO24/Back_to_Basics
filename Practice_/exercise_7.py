"""

Objective - Think in arrays, not loops

Tasks
-Extract revenue into a NumPy array
-Use boolean masking to select
    -Orders with revenue > 2000

-Calculate total revenue and average revenue per order

"""

import numpy as np
import pandas as pd

# Lets fetch and load the data
df = pd.read_csv('combined_data.csv')
df['revenue'] = df['units_sold'] * df['price']

# Lets extract revenue into a numpy array
arr = np.array([df['revenue']])
print("\nRevenue in array format: ", arr)

mask = df['revenue'] > 2000
high_revenue_orders = df[mask]
print("\nMasking revenue: ", high_revenue_orders)

total_revenue = df['revenue'].sum()
average_revenue = df['revenue'].mean()
order_count = len(df)

print(f"\nTotal Revenue: ${total_revenue:,.2f}")
print(f"Average Revenue per Order: ${average_revenue:,.2f}")
print(f"Total Number of Orders: {order_count}")


