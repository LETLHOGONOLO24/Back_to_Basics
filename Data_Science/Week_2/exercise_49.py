"""

Objective - Understand drivers of performance
Tasks
-Create scatter plot of speed vs error rate
-Size points by units processed

-Color by department
-Annotate top 2 performers

"""

import pandas as pd
import matplotlib.pyplot as plt

# Lets load the data
df = pd.read_csv('performance_day8.csv')
df['speed_score'] = 1 / df['avg_processing_time']
df['error_rate'] = df['errors_made'] / df['units_processed']

# Lets Normalize
def normalize(col):
    return (col - col.min()) / (col.max() - col.min())

df['units_norm'] = normalize(df['units_processed'])
df['error_rate_norm'] = normalize(df['error_rate'])
df['speed_norm'] = normalize(df['speed_score'])

# Lets create a composite score
df['composite_score'] = (0.5 * df['units_norm']) + \
                        (0.5 * df['speed_norm']) + \
                        (0.2 * (1 - df['error_rate_norm']))

# Lets identify top 2 performers (using composite score logic)
top_2 = df.sort_values('composite_score', ascending=False).head(2)

# Lets create the scatter plot
plt.figure(figsize=(10, 6))

# Lets define colors for departments
colors = {'Sales': 'orange', 'Operations': 'blue'}

# Scatter points: X=Speed, Y=Error Rate
# s=Size (scaled for visibility), c=Color mapped to department
plt.scatter(df['speed_score'], df['error_rate'],
            s=df['units_processed'] * 2,
            c=df['department'].map(colors),
            alpha=0.6, edgecolors='black')

# Lets annote Top 2 Performers
for i, row in top_2.iterrows():
    plt.annotate(row['employee_name'],
                 (row['speed_score'], row['error_rate']),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center',
                 fontweight='bold')
    
# Lets format
plt.title('Employee Performance Matrix: Speed vs Error Rate', fontsize=14)
plt.xlabel('Speed (1 / Avg Processing Time)')
plt.ylabel('Error Rate (Errors / Units)')
plt.grid(True, linestyle='--', alpha=0.5)

# Adding a manual legend for colors
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color='w', label=k,
                          markerfacecolor=v, markersize=10) for k, v in colors.items()]
plt.legend(handles=legend_elements, title="Department")
plt.tight_layout()
plt.show()