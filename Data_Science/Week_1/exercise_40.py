"""

Objective - Understand relative standing.
Tasks
-Convert efficiency_score to a NumPy array.

-Calculate 25th, 50th, 75th percentiles
-Classify employees as bottom 25%, middle 50%, top 25%

"""

import numpy as np
import pandas as pd

# Lets load the data
df = pd.read_csv('performance_day7.csv')
df['efficiency_score'] = df['units_processed'] / (df['errors_made'] + 1)

# Lets convert to NumPy array
eff_arr = df['efficiency_score'].values

# Lets calculate 25th, 50th, and 75th percentile
p25 = np.percentile(eff_arr, 25)
p50 = np.percentile(eff_arr, 50)
p75 = np.percentile(eff_arr, 75)

print(f"\nP25 (Bottom Threshold): {p25:.2f}")
print(f"P50 (Median): {p50:.2f}")
print(f"P75 (Top Threshold): {p75:.2f}")

# Lets classify using np.select which is cleaner than multiple Ifs
conditions = [
    (df['efficiency_score'] <= p25),
    (df['efficiency_score'] > p25) & (df['efficiency_score'] < p75),
    (df['efficiency_score'] >= 75)
]

choices = ['Bottom 25%', 'Middle 50%', 'Top 25%']
# NumPy refuses to store words and numbers in the same column, so we have to tell it that default="Unknown" to prevent an error
# np.select() is an alternative to a long list of if/else
df['performance_tier'] = np.select(conditions, choices, default="Unknown")

print(df[['employee_name', 'efficiency_score', 'performance_tier']].sort_values('efficiency_score', ascending=False))