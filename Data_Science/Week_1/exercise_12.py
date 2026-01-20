"""

Objective - Reinforce array-based thinking

Tasks
-Convert revenue into a NumPy array
-Create a new NumPy array where "High" if revenue > 3000 and "Low" otherwise
-Count how many "High" revenue transactions exist

"""

import pandas as pd
import numpy as np

# Lets load the data
df = pd.read_csv('sales_day3_filled.csv')

# Lets convert revenue into a NumPy array
revenue = np.array([df['revenue']])
print(f"\nLets see revenue as an array:\n {revenue}")

# Lets create a new NumPy array
revenue_labels = np.where(revenue > 3000, "High", "Low")

# Count how many "High" revenue transactions exist
high_count = np.sum(revenue_labels == "High")

print(f"\nNumber of High revenue transactions:\n {high_count}")
print(f"\nRevenue labels array:\n {revenue_labels}")
    