"""

Objective - Visualize differences
Tasks
-Create boxplot of processing time by department

-Overlay mean values
-Interpret overlap

"""

import pandas as pd
import matplotlib.pyplot as plt

# Lets load the data
df = pd.read_csv('performance_day9.csv')

# Lets extract data for boxplot
sales_times = df[df['department'] == 'Sales']['avg_processing_time']
ops_times = df[df['department'] == 'Operations']['avg_processing_time']

# Create Boxplot
plt.figure(figsize=(8, 6))
# showmeans=True adds a marker for the mean automatically
plt.boxplot([sales_times, ops_times], labels=['Sales', 'Operations'],
            patch_artist=True, showmeans=True,
            meanprops={"marker":"o", "markerfacecolor":"red", "markeredgecolor":"black"})

# Lets format this bad boy
plt.title('Processing Time Distribution by Department', fontsize=12)
plt.ylabel('Average Processing Time (mins)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.show()