"""

Objective - Visualize model fit
Tasks
-Create scatter plot for training hours vs error rate

-Overlay regression line
-Color points by department

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lets load the data and calculate error rate
df = pd.read_csv('performance_day11.csv')
df['error_rate'] = df['errors_made'] / df['units_processed']

# Lets compute the Regression Line (y = mx + c)
slope, intercept = np.polyfit(df['training_hours'], df['error_rate'], 1)
line_x = np.array(df['training_hours'].min(), df['training_hours'].max())
line_y = slope * line_x + intercept

# Map colors to departments
colors = {'Sales': '#ff7f0e', 'Operations': '#1f77b4'}

# Plot each department separately to create the legend labels
for dept, group in df.groupby('department'):
    plt.scatter(group['training_hours'], group['error_rate'],
                label=dept, color=colors[dept], s=100, edgecolors='black')
    
# Plot the regression line
plt.plot(line_x, line_y, color='red', linestyle='--', label='Regression Line')

# Labels and Formatting
plt.title('Training Hours vs. Error Rate by Department', fontsize=14)
plt.xlabel('Training Hours', fontsize=12)
plt.ylabel('Error Rate (Errors/Units)', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()