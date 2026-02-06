"""

Objective - Prepare clean, model-ready data
Tasks
-Load the CSV
-Create error_rate = errors_made / units_processed

-Select features:
    training_hours
    avg_processing_time

-Define target variable: error_rate
-Check correlations

"""

import pandas as pd

# Lets import the data
df = pd.read_csv('performance_day11.csv')
df['error_rate'] = df['errors_made'] / df['units_processed']

# Lets select Features and Target
features = ['training_hours', 'avg_processing_time']
target = 'error_rate'

# Lets check correlations
# We select the columns of interest and use the .corr() method
correlation_matrix = df[features + [target]].corr()

print("Correlation with Error Rate:")
print(correlation_matrix[target].drop(target))

# When you run df.corr(), Pandas creates a square table (a Correlation Matrix)
# where every column is compared to every other column.

# correlation_matrix[target] filters the big table down to just one column
# .drop(target) drops that 1.00 row

# We already know that error_rate is 100% correlated with itself—that’s not
# useful information for our analysis.
# By "dropping" it, we are left with only the actual relationships we want
# dd .to study (like training_hours and avg_processing_time).