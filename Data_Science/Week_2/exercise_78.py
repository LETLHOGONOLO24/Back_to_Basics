"""

Objective - Fit multiple regression manually
Tasks
-BUild feature matrix X (include intercept)
-COmpute coefficients using:
    β = (XᵀX)⁻¹Xᵀy

-Interpret which coefficient is largest?
-Predict revenue for:
    units_sold = 145
    discount = 8

    ad_spend = 2150
    visits = 54

"""

import pandas as pd
import numpy as np

# 1. Load the data
df = pd.read_csv('sales_day12.csv')

# 2. Build feature matrix X (Include intercept)
# Features: units_sold, discount_pct, ad_spend, customer_visits
X_raw = df[['units_sold', 'discount_pct', 'ad_spend', 'customer_visits']].values
ones = np.ones((X_raw.shape[0], 1))
X = np.c_[ones, X_raw]  # Add column of 1s for the intercept

# 3. Target vector y
y = df['revenue'].values

# 4. Compute coefficients using the Normal Equation: β = (XᵀX)⁻¹Xᵀy
XTX = X.T @ X
XTX_inv = np.linalg.inv(XTX)
XTy = X.T @ y
beta = XTX_inv @ XTy

# 5. Predict for specific values
# units_sold=145, discount=8, ad_spend=2150, visits=54
new_obs = np.array([1, 145, 8, 2150, 54])
prediction = new_obs @ beta

print(f"Coefficients: {beta}")
print(f"Prediction: {prediction:.2f}")