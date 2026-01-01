"""

*Objective - First visualizations

*Tasks
-Plot a bar chart of total revenue per product
-Label axes and add a title
-Rotate x-axis labels for readability

"""

import numpy as np
import matplotlib.pyplot as plt

# Lets load the data
data = np.genfromtxt('sales_day1.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

# Lets access the specific columns
units_sold = data['units_sold']
price = data['price']
product = data['product']

# Lets calculate total revenue per row
total_revenue = units_sold * price

# Lets plot the data
x = product
y = total_revenue

plt.bar(x,y)
plt.title("Total Revenue per product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.show()

# Chatbot says using Pandas is waaay better