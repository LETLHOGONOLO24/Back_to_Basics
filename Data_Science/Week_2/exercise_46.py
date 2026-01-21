"""

Objective - Build a composite performance score
Tasks
-Load the CSV
-Create features
    error_rate = errors_made / units_processed
    speed_score = 1 / avg_processing_time

-Normalize
    units_processed
    error_rate
    speed_score

-Create a composite score
    score = (0.5 * units_norm)
        + (0.3 * speed_norm)
        + (0.2 * (1 - error_rate_norm))
-Rank employees by score

"""

import pandas as pd

# Lets load the data
df = pd.read_csv('performance_day8.csv')

# Lets create features
df['error_rate'] = df['errors_made'] / df['units_processed']
df['speed_score'] = 1 / df['avg_processing_time']

# Lets Normalize
def normalize(col):
    return (col - col.min()) / (col.max() - col.min())

df['units_norm'] = normalize(df['units_processed'])
df['error_rate_norm'] = normalize(df['error_rate'])
df['speed_norm'] = normalize(df['speed_score'])

# Lets create a composite score
df['composite_score'] = (0.5 * df['units_norm']) + \
                        (0.5 * df['speed_norm']) + \
                        (0.2 * (1 - df['error_rate_norm']))

# Lets rank employees by score
df['performance_rank'] = df['composite_score'].rank(ascending=False).astype(int)

# Lets view the final leaderboard
leaderboard = df[['employee_name', 'composite_score', 'performance_rank']].sort_values('performance_rank')
print(leaderboard)