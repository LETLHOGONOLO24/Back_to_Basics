"""

Objective - Understand regression mechanics
Tasks
-Use NumPy to model error_rate ~ training_hours
-Compute
    Slope
    Intercept

Predict error rate for 16 training hours

"""

import numpy as np
import pandas as pd

# Lets load the data
df = pd.read_csv('performance_day11.csv')
df['error_rate'] = df['errors_made'] / df['units_processed']

# Lets extract x and y as NumPy arrays
x = df['training_hours'].values
y = df['error_rate'].values

# Lets compute Slope (m) and Intercept (c)
# np.polyfit finds the 'line of best fit'. The '1' means linear
slope, intercept = np.polyfit(x, y, 1)

# Lets predict error rate for 16 hours
training_val = 16
prediction = (slope * training_val) + intercept

print(f"\nSlope: {slope:.5f}")
print(f"Intercept: {intercept:.5f}")
print(f"Prediction for 16hrs: {prediction:.5f}")