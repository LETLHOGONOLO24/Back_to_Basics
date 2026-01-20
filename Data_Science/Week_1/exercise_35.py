"""

Objective - Spot inefficiencies visually
Tasks
-Create a bar chart for efficiency score per employee

-Add horizontal line for average efficiency
-Highlight underperformers


"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lets load the data
emp_df = pd.read_csv('employees_day6.csv')
tns_df = pd.read_csv('transactions_day6.csv')

# Lets merge the CSV files
df = pd.merge(tns_df, emp_df, on='employee_id')

# Lets fill in the missing units
df['units_processed'] = df['units_processed'].fillna(
    df.groupby('department')['units_processed'].transform('mean')
)

# Lets calculate efficiency
df['efficiency_score'] = df['units_processed'] / (df['errors_made'] + 1)

# Aggregate per Employee
emp_stats = df.groupby('employee_name')['efficiency_score'].mean().reset_index()

# Calculate Benchmarks
avg_efficiency = emp_stats['efficiency_score'].mean()
std_efficiency = emp_stats['efficiency_score'].std()
threshold = avg_efficiency - std_efficiency

plt.figure(figsize=(10, 6))
# Highlight logic: Red if below threshold, Blue otherwise
colors = ['#ff4d4d' if score < threshold else '#4da6ff' for score in emp_stats['efficiency_score']]

plt.bar(emp_stats['employee_name'], emp_stats['efficiency_score'], color=colors)

# Lets add benchmark lines
plt.axhline(avg_efficiency, color='black', linestyle='--', label=f'Avg Efficiency ({avg_efficiency:.1f})')
plt.axhline(threshold, color='red', linestyle=':', label=f'Underperformance Line ({threshold:.1f})')

plt.title('Performance Benchmark: Efficiency per Employee', fontsize=15)
plt.ylabel('Efficiency Score')
plt.legend()

plt.show()