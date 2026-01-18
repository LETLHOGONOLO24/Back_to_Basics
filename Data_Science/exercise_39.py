"""

Objective - Compare employees fairly
Tasks
-Load the CSV

-Create metrics:
    error_rate = errors_made / units_processed
    efficiency_score = units_processed

-Normalize efficiency_score using min-max scaling
-Rank employees by efficiency (highest = rank 1)

"""

import pandas as pd

# Lets load the data
df = pd.read_csv('performance_day7.csv')

# Creating metrics
df['error_rate'] = df['errors_made'] / df['units_processed']
df['efficiency_score'] = df['units_processed'] / (df['errors_made'] + 1)

print(f'\nEfficiency_Score: {df['efficiency_score'].head(6)}')

# Lets normalize efficiency_score
# This squeezes the scores into a 0 to 1 range
min_val = df['efficiency_score'].min()
max_val = df['efficiency_score'].max()

# The numerator shifts the data so that the lowest person starts at zero
# The denominator calculates the total distance between the best and worst person
df['normalized_efficiency'] = (df['efficiency_score'] - min_val) / (max_val - min_val)

# Lets rank employees (Highest score = Rank 1) - ascending=False because a rank = 1 is the winner
df['efficiency_rank'] = df['efficiency_score'].rank(ascending=False, method='min').astype(int)

# Lets sort and view
df_results = df.sort_values('efficiency_rank')
print(df_results[['employee_name', 'efficiency_score', 'normalized_efficiency', 'efficiency_rank']])



