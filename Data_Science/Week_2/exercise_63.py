"""

Objective - Quantify how big the difference is
Tasks
-Compute Cohen's d for processing time between departments
-Interpret small, medium and large effect

"""

import numpy as np
import pandas as pd

# Lets load the data
df = pd.read_csv('performance_day10.csv')

# Lets extract the groups into NumPy arrays
sales = df[df['department'] == 'Sales']['avg_processing_time'].values
ops = df[df['department'] == 'Operations']['avg_processing_time'].values

# Lets calculate means and variances
n1, n2 = len(sales), len(ops)
m1, m2 = np.mean(sales), np.mean(ops)
v1, v2 = np.var(sales, ddof=1), np.var(ops, ddof=1)

# Lets calculate pooled standard deviation
# This is the average spread of both groups combined
pooled_std = np.sqrt(((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2))

# Lets calculate Cohen's d
# d = (Mean Difference) / (Standard Deviation)
cohens_d = (m1 - m2) / pooled_std

print(f"\nCohen's d: {cohens_d:.4f}")