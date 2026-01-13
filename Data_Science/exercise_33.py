"""

Objective - Use statistics for performance monitoring
Tasks
-Convert efficiency_score to a NumPy array

-Calculate mean efficiency and standard deviation
-Flag employees who are below (mean - 1 std)

"""

import numpy as np
import pandas as pd

# Lets load the data
emp_df = pd.read_csv('employees_day6.csv')
trans_df = pd.read_csv('transactions_day6.csv')

# Lets merge the CSV files
df = pd.merge(trans_df, emp_df, on='employee_id')

# Lets fill the empty units_processed before calculating efficiency
df['units_processed'] = df['units_processed'].fillna(
    df.groupby('department')['units_processed'].transform('mean')
)

# Lets convert efficiency_score to a NumPy array
# We use .values to grab the raw data without the index/labels
df['efficiency_score'] = df['units_processed'] / (df['errors_made'] + 1)
efficiency_arr = df['efficiency_score'].values

# Lets calculate Statistics
mean_eff = np.mean(efficiency_arr)
std_eff = np.std(efficiency_arr)

print(f"\nMean Efficiency: {mean_eff:.2f}")
print(f"Standard Deviation: {std_eff:.2f}")

# Define the "Underperformance" Threshold
threshold = mean_eff - std_eff
print(f"\nFlagging Threshold: {threshold:.2f}\n")

# Flag employees who are below the threshold
df['underperformance_flag'] = np.where(df['efficiency_score'] < threshold, "Review Required", "Performing")

# Show the results
print(df[['employee_name', 'efficiency_score', 'underperformance_flag']])