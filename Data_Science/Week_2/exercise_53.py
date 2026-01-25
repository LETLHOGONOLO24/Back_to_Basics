"""

Objective - Prepare data for statistical testing
Tasks
-Load the CSV
-Create error_rate = errors_made / units_processed

-Group by department and compute
    -Mean error rate
    -Mean processing time
-Visually inspect differences

"""

import pandas as pd
import matplotlib.pyplot as plt

# Lets load the data
df = pd.read_csv('performance_day9.csv')

# lets create error_rate feature
df['error_rate'] = df['errors_made'] / df['units_processed']

# Lets Group by department and compute means
dept_metrics = df.groupby('department')[['error_rate', 'avg_processing_time']].mean()
print('\n--- Department Performance Summary ---')
print(dept_metrics)

# Visual Inspection (Basic plot)
dept_metrics.plot(kind='bar', subplots=True, figsize=(8, 8),
                  title="Departmental Differences", layout=(2, 1))
plt.tight_layout()
plt.show()
