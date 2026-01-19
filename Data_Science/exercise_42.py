"""

Objective - See performance spread
Tasks
-Create a histogram of efficiency scores

-Overlay vertical lines for 25th and 75th percentiles
-Create a bar chart: efficiency score by employee (sorted)

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lets load the data
df = pd.read_csv('performance_day7.csv')
df['efficiency_score'] = df['units_processed'] / (df['errors_made'] + 1)

# Lets calculate percentiles for the Histogram lines
p25 = np.percentile(df['efficiency_score'], 25)
p75 = np.percentile(df['efficiency_score'], 75)

# --- CHART 1: Histogram ---
plt.hist(df['efficiency_score'], bins=5, color='skyblue', edgecolor='black')

# Overlay the vertical lines
plt.axvline(p25, color='red', linestyle='--', label=f'p25 ({p25:.1f})')
plt.axvline(p75, color='green', linestyle='--', label=f'p75 ({p75:.1f})')

plt.title('Performance Distribution (Efficiency)')
plt.xlabel('Efficiency Score')
plt.ylabel('Number of Employees')
plt.legend()
plt.show()
plt.close()

# --- CHART 2: Sorted Bar Chart ---
# Sorting first is key for professional visuals
df_sorted = df.sort_values('efficiency_score', ascending=False)

plt.bar(df_sorted['employee_name'], df_sorted['efficiency_score'], color='teal')
plt.title('Employee Ranking by Efficiency')
plt.ylabel('Efficiency Score')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()