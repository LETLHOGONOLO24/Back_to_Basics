"""

Objective - Efficient model calculation
Tasks
-Convert features into Numpy arrays
-Perform min-max normalization using NumPy

-Compute the composite score using vectorized operations
-Verify results match Pandas output

"""

import numpy as np
import pandas as pd

# Lets load the data
df = pd.read_csv('performance_day8.csv')
df['error_rate'] = df['errors_made'] / df['units_processed']
df['speed_score'] = 1 / df['avg_processing_time']

#Lets convert features into NumPy arrays
units = df['units_processed'].values
errors = df['error_rate'].values
speed = df['speed_score'].values

# Lets normalize
"""
Normalizing means leveling the playing field, we squash every different
unit of measurement into a scale of 0 to 1

0 is the worst score
1 is the best score
"""
u_norm = (units - np.min(units)) / (np.max(units) - np.min(units))
e_norm = (errors - np.min(errors)) / (np.max(errors) - np.min(errors))
s_norm = (speed - np.min(speed)) / (np.max(speed) - np.min(speed))

df['composite_score'] = (0.5 * u_norm) + \
                        (0.3 * s_norm) + \
                        (0.2 * (1 - e_norm))
# Lets compute composite score (Vectorized)
# Every operation happens to the entire array at once
composite_scores = (0.5 * u_norm) + (0.3 * s_norm) + (0.2 * (1 - e_norm))

# Lets check if the NumPy array matches our previous Pandas column
print(f"\nMatch Verified: {np.allclose(composite_scores, df['composite_score'])}")

"""
np.allclose() checks if two arrays are element-wise equal within a very small
tolerance
-It asks, are these numbers close enough that the difference is just a tiny
rounding error, if yes then it returns true

"""