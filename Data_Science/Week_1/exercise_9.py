"""

Objective - Move beyond single plots

Task
-Create a bar chart = total revenue per customer
-Create a second chart = total units sold per product
-Ensure titles and axis labels

"""

import matplotlib.pyplot as plt
import pandas as pd

# Lets load the data
df = pd.read_csv('combined_data.csv')

df['revenue'] = df['units_sold'] * df['price']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Units Sold
ax1.bar(df['customer_name'], df['revenue'], color='skyblue')
ax1.set_title('Revenue per customer')
ax1.set_ylabel('Revenue')

# Plot 2: Units Sold
ax2.bar(df['product'], df['units_sold'], color='salmon')
ax2.set_title('Total units sold per product')
ax2.set_ylabel('Units_sold')

plt.tight_layout()
plt.show()