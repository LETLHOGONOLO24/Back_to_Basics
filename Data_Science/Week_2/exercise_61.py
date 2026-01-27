"""

Objective - Estimate uncertainty, not just averages
Tasks
-Load the CSV
-Group by department

-Compute Mean processing time and Standard error
-Construct 95% confidence intervals for each department
-Compare interval overlap

"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Lets load the data
df = pd.read_csv('performance_day10.csv')

# Lets compute the mean and standard error (SEM)
# SEM = Std Deviation / Square Root of Sample Size
# The aggregate() method allows you to run multiple calculations at once like
# finding the mean, count, and std of each department
stats_df = df.groupby('department')['avg_processing_time'].agg(['mean', 'count', 'std'])
print("\nStats DataFrame")
print(stats_df)

# agg() also created new columns like stats_df['std'] and stats_df['count']
# When looking for sem, we're going to look for it for both departments
stats_df['sem'] = stats_df['std'] / np.sqrt(stats_df['count'])
print("\nStandard Error")
print(stats_df['sem'])

# Lets construct 95% Confidence Intervals
# We use the t-distribution because our sample sizes (4 per dept) are small
confidence = 0.95
stats_df['ci_margin'] = stats.t.ppf((1 + confidence) / 2, stats_df['count'] - 1) * stats_df['sem']

stats_df['ci_lower'] = stats_df['mean'] - stats_df['ci_margin']
stats_df['ci_upper'] = stats_df['mean'] + stats_df['ci_margin']

print(stats_df[['mean', 'sem', 'ci_lower', 'ci_upper']])

# Lets visualize the Overlap
plt.errorbar(stats_df.index, stats_df['mean'], yerr=stats_df['ci_margin'], fmt='o', capsize=5)
plt.title("95% CI of Processing Time")
plt.show()