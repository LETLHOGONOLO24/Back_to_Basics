"""

Objective - Statistical regression output
Tasks
-Perform linear regression using SciPy
-Extract Coefficient, p-value, R squared

-Interpret is training statistically significant

"""

import pandas as pd
from scipy import stats

# Lets load the data and create error_rate
df = pd.read_csv('performance_day11.csv')
df['error_rate'] = df['errors_made'] / df['units_processed']

# Lets perform Linear Regression
# lingress returns 5 values; we focus on the slope, p-value, and r-value
slope, intercept, r_value, p_value, std_err = stats.linregress(df['training_hours'], df['error_rate'])

# Lets extract requested metrics
r_squared = r_value**2

print(f"\nCoefficient (slope): {slope:.6f}")
print(f"p-value: {p_value:.6f}")
print(f"R squared (Coefficient of Determination): {r_squared:.6f}")

"""

🔍 Is training statistically significant?

Yes, absolutely. Here is why:

The p-value Rule: In statistics, a p-value less than $0.05$ means the result is "statistically significant."
Our p-value is $0.0009$, which is roughly 50 times smaller than the threshold. This tells us there is a $99.9\%$
chance that the link between training and fewer errors is real and not just a random fluke.

The Power of R-squared: An R-squared of $0.86 is exceptionally high. It means that if you want to know why one
employee makes more mistakes than another, 86% of the answer lies simply in how much training they received.
The remaining 14% is due to other factors (like individual talent or equipment issues).

"""