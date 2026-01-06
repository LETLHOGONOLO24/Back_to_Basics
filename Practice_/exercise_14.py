"""

Objective - Visualize change over time
Tasks
-Plot a line chart of daily total revenue

-Highligh days with revenue > 5000
-Add Grid and Markers

"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. Read and prepare data
df = pd.read_csv('sales_day3_filled.csv')
df['date'] = pd.to_datetime(df['date'])

# 2. Get daily revenue
daily = df.groupby('date')['revenue'].sum().reset_index() # daily is a pandas series with index as the dates, values as total revenue for each date

# 3. Create the plot
plt.figure(figsize=(10, 5))

# Line chart with markers
plt.plot(daily['date'], daily['revenue'], 'o-', linewidth=2, markersize=6)

# Highlight points above 5000
high_revenue = daily[daily['revenue'] > 5000]
plt.plot(high_revenue['date'], high_revenue['revenue'], 'ro', markersize=10)

# Add grid
plt.grid(True, alpha=0.3) # Alpha controls transparency/opacity of elements in the plot

# Labels
plt.title('Daily Revenue')
plt.xlabel('Date')
plt.ylabel('Revenue')

# Rotate date labels
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()