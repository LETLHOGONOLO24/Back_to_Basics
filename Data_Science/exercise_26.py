"""

Objective - Understand what correlation really is
Tasks
-Extract marketing_spend and revenue as NumPy arrays

-Compute correlation using np.corrcoef
-Compare results with Pandas output

"""

import numpy as np
import pandas as pd

# lets load the data
df = pd.read_csv('sales_day5.csv')

# Lets use .values to convert a Pandas series to a NumPy array
marketing_arr = df['marketing_spend'].values
revenue_arr = df['revenue'].values

# lets compute correlation using np.corrcoef
corr_matrix = np.corrcoef(marketing_arr, revenue_arr)

# We grab the value at row 0, column 1 (the relationship between the two variables)
np_corr_value = corr_matrix[0, 1]

# Lets compare with Pandas output
pd_corr_value = df['marketing_spend'].corr(df['revenue'])

print(f"\nNumPy Correlation: {np_corr_value:.6f}")
print(f"Pandas Correlation: {pd_corr_value:.6f}")


