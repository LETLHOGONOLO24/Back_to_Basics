"""

Objectives - Visualize correlation
Tasks
-Create a scatter plot of marketing spend vs Revenue

-Color points by category
-Add trend line and labels

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lets load the data
df = pd.read_csv('sales_day5.csv')
df['revenue'] = df['units_sold'] * df['price']

# 'hue' colors the points by category
# 'lmplot' automatically adds the linear regression (trend) lines
plot = sns.lmplot(
    data=df,
    x='marketing_spend',
    y='revenue',
    hue='category',
    height=6,
    aspect=1.5
)

# Lets add Labels and Title
plt.title('Marketing Spend vs Revenue: Category Analysis', fontsize=15)
plt.xlabel('Marketing Spend (Rand)', fontsize=12)
plt.ylabel('Total Revenue (Rand)', fontsize=12)

# Lets show/save the plot
plt.show()