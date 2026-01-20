"""

Objective - Visual comparison of raw vs smoothed data
Task
-Plot daily revenue as a line chart

-Plot the 3-day rolling average on the same chart
-Add legend, grid, and clear title

"""

import pandas as pd
import matplotlib.pyplot as plt

# Lets load the data
df = pd.read_csv('sales_day4.csv')

# Change date to datetime
df['date'] = pd.to_datetime(df['date'])

# Lets add revenue column
df['revenue'] = df['units_sold'] * df['price']

# Get daily revenue
daily = df.groupby('date')['revenue'].sum().reset_index()
daily = daily.sort_values('date')

# Lets calculate 3-day rolling average
daily['rolling_avg'] = daily['revenue'].rolling(3).mean()

# Create the plot
plt.figure(figsize=(12, 6))

# Line chart with markers
plt.plot(daily['date'], daily['revenue'], 'o-', linewidth=2, markersize=6, label='Daily Revenue')

# Lets plot rolling average
plt.plot(daily['date'], daily['rolling_avg'], 'r--', linewidth=3, label='3-Day Rolling Average')

# Lets add features
plt.title('Daily Revenue with 3-Day Moving Average', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Revenue (R)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend()

# Lets format dates
plt.gcf().autofmt_xdate() # Auto rotate dates

plt.tight_layout()
plt.show()