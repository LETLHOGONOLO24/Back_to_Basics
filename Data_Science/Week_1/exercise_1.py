"""

Getting comfortable with NumPy arrays and basic operations

Tasks
- Load  units_sold and price into NumPy arrays
- Calculate total revenue per row (units_sold * price)
- Compute Mean revenue, Max revenue, and min revenue

"""

import numpy as np
import pandas as pd

# Lets load the data
# Delimiter=',' tells us to look for commas
# names=True tells it to treat the first row as headers

data = np.genfromtxt('sales_day1.csv', delimiter=',', names=True)

# Access the specific columns
units_sold = data['units_sold']
price = data['price']

# Lets calculate total revenue per row
total_revenue = units_sold * price
print("Total Revenue per row: ", total_revenue)

mean_revenue = np.mean(total_revenue)
max_revenue = np.max(total_revenue)
min_revenue = np.min(total_revenue)

print("Mean Revenue: ", mean_revenue)
print("Max Revenue: ", max_revenue)
print("Min Revenue: ", min_revenue)