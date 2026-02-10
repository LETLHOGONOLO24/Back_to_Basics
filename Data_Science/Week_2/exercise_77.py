"""

Objective - Prepare features and detect potential issues
Tasks
-Load dataset
-Select predictors:
    units_sold

    discount_pot
    ad_spend
    customer_visits

-Target variable
    revenue

-Check:
    Correlation matric
    Highly correlated predicitons

"""

import pandas as pd

# Lets load the dataset
df = pd.read_csv('sales_day12.csv')

# Select predictors
features = ['units_sold', 'discount_pct', 'ad_spend', 'customer_visits']
X = df[features]

# Target revenue
Y = df['revenue']

# Combine X and Y temporarily to see how features relate to Revenue
analysis_df = X.copy()
analysis_df['revenue'] = Y

# Generate the correlation matrix
corr_matrix = analysis_df.corr()
print("\nCorrelation Matrix")
print(corr_matrix)
