"""

Objectives - Intuitive confidence intervals
Tasks
-Extract processing times for Operations
-Perform bootstrap resampling (e.g. 1000 samples)

-Compute bootstrap mean distribution
-Extract 2.5th and 97.5th percentiles

"""

import pandas as pd
import numpy as np

# Lets load the data
df = pd.read_csv('performance_day10.csv')

# Lets extract processing times for Operations as a NumPy array
ops_times = df[df['department'] == 'Operations']['avg_processing_time'].values

# Lets perform bootstrap resampling
n_iterations = 1000
bootstrap_means = []

for i in range(n_iterations):
    # Sample 4 times from ops_times WITH replacement
    sample = np.random.choice(ops_times, size=len(ops_times), replace=True)
    # Compute the mean of this specific sample
    bootstrap_means.append(np.mean(sample))

# Convert list to NumPy array for easier math
# NumPy allows us to do advanced math like finding percentiles faster than Lists
bootstrap_means = np.array(bootstrap_means)

# Lets extract the 2.5th and 97.5th percentiles (The 95% CI)
ci_lower = np.percentile(bootstrap_means, 2.5)
ci_upper = np.percentile(bootstrap_means, 97.5)

print(f"Original Operations Mean: {np.mean(ops_times):.2f}")
print(f"Bootstrap 95% Confidence Interval: [{ci_lower:.2f}, {ci_upper:.2f}]")