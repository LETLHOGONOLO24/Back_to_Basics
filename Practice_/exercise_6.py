"""

Objective - Learning how datasets come together in real projects

Tasks
-Load both csv files into Pandas
-Covert order_date to datetime
-Merge orders with customers using customer_id
-Create a new column: revenue = units_sold * price

"""

import pandas as pd
import datetime

# lets load the data from the csv files
df_customers = pd.read_csv('customers_day2.csv')
df_orders = pd.read_csv('orders_day2.csv')

#Lets convert order_date to datetime
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])

# Lets merge the 2 csv files
merged_df = pd.merge(df_customers, df_orders, on='customer_id', how='left')
merged_df.to_csv('combined_data.csv', index=False)

# Lets create a revenue = units_sold * price column
df_combined = pd.read_csv('combined_data.csv') 
df_combined['revenue'] = df_combined['units_sold'] * df_combined['price']
