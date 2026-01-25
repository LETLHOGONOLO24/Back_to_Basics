"""

Objective - Test if departments differ fully
Hypothesis:
    -H0: No difference in average processing time between departments
    -H1 (Alt): A difference exists

Tasks
-Perform an independent t-test
-Record test statistic and p-value
-Decide to reject or fail to reject H0 (alpha = 0.05)

"""

import pandas as pd
from scipy import stats

# Lets load the data
df = pd.read_csv('performance_day9.csv')

# Lets extract arrays for the two groups
sales_time = df[df['department'] == 'Sales']['avg_processing_time'].values
ops_time = df[df['department'] == 'Operations']['avg_processing_time'].values

print("\nSales Time")
print(sales_time)
print("\nOperations Time")
print(ops_time)

# Lets perform independent T-test
# This compares the means of two independent groups
t_stat, p_val = stats.ttest_ind(sales_time, ops_time)

print(f"\nTest Statistic: {t_stat:.4f}")
print(f"P-value: {p_val:.4f}\n")

# Lets write the decision logic
alpha = 0.05
if p_val < alpha:
    print("Decision: Reject H0 (Difference is statistically significant)")
else:
    print("Decision: Fail to Reject H0 (Difference could be due to change)")