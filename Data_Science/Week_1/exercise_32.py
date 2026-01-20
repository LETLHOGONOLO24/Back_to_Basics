"""

Objective - Clean operational data and compute performance metrics.
Tasks
-Load both CSVs
-Convert date to datetime

-Identify missing units_processed
-Fill missing units_processed with department-level mean

-Merge transactions with employees
-Create metrics:

    -error_rate = errors_made / units_processed
    -efficiency_score = units_processed / (errors_made + 1)

"""

import pandas as pd

# Lets load both CSVs
df_employees_day6 = pd.read_csv('employees_day6.csv')
df_transactions_day6 = pd.read_csv('transactions_day6.csv')

# Lets convert date to datetime
df_transactions_day6['date'] = pd.to_datetime(df_transactions_day6['date'])

# Lets merge transactions with employees to get the department for each row
df = pd.merge(df_transactions_day6, df_employees_day6, on='employee_id')

# Lets fill missing units_processed with Department-level mean
# .transform('mean') calculates the mean for each group and maps it back to the original rows
df['units_processed'] = df['units_processed'].fillna(
    df.groupby('department')['units_processed'].transform('mean')
)

# Create metrics
# Error Rate: How many errors per unit processed
df['error_rate'] = df['errors_made'] / df['units_processed']

# Efficiency Score: Units processed adjusted for errors (adding 1 avoids division by zero)
df['efficiency_score'] = df['units_processed'] / (df['errors_made'] + 1)

print(df[['transaction_id', 'employee_id', 'department', 'units_processed', 'error_rate', 'efficiency_score']])
# The other [] mean lets put the list in the DataFrame because in Python you use [] to create a list