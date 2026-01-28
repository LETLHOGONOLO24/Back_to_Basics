"""

Objective - Visualize confidence
Tasks
-Plot mean processing time per department

-Add error bars (confidence intervals)
-Interpret overlap visually

"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Lets load the data
df = pd.read_csv('performance_day10.csv')

# Lets calculate Mean, SEM, and CI Margin
stats_df = df.groupby('department')['avg_processing_time'].agg(['mean', 'std', 'count'])
stats_df['sem'] = stats_df['std'] / np.sqrt(stats_df['count'])
print("Count\n")
print(stats_df['count'])

# Lets calculate 95% Confidence Interval Margin using t-distribution
confidence = 0.95
stats_df['ci_margin'] = stats.t.ppf((1 + confidence) / 2, stats_df['count'] - 1) * stats_df['sem']
print("CI Margin\n")
print(stats_df['ci_margin'])

# Lets create the plot
plt.figure(figsize=(8, 6))
plt.bar(stats_df.index, stats_df['mean'],
        yerr=stats_df['ci_margin'], # This adds the error bars
        capsize=10,
        color=['#4da6ff', '#ffb366'],
        edgecolor='black', alpha=0.8)

plt.title('Mean Processing Time by Department (95% CI)', fontsize=14)
plt.ylabel('Avg Processing Time (minutes)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.show()