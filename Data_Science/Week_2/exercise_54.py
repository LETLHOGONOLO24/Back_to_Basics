"""

Objective - Check assumptions
Tasks
-Extract avg_processing_time into NumPy arrays:
    -Sales
    -Operations

-Compute Mean and Standard deviation
-Compare spread and central tendency

"""

import pandas as pd
import numpy as np

# Lets load the data
df = pd.read_csv('performance_day9.csv')

# Lets extract into NumPy arrays
sales_time = df[df['department'] == 'Sales']['avg_processing_time'].values
ops_time = df[df['department'] == 'Operations']['avg_processing_time'].values

# Lets compute statistics
stats = {
    "Sales": {"mean": np.mean(sales_time), "std": np.std(sales_time)},
    "Operations": {"mean": np.mean(ops_time), "std": np.std(ops_time)}
}

for dept, s in stats.items():
    print(f"\n{dept} -> Mean: {s['mean']:.2f}, Std Dev: {s['std']:.2f}")

"""

The stats.items() is a method used to loop through a dictionary

The filter: df['department'] == 'Sales' - this part creates a boolean mask.
It goes through the department column and asks every row, "Are you Sales?"
It returns a list of True and False

The slice: df[...] - When you wrap that mask inside df[], you are telling
Pandas "Keep only the rows where the answer was True". At this stage, you
have a smaller DataFrame that only contains Sales employees (Thabo, Naledi,
and Lerato)

The Selection: ['avg_processing_time'] - Now that you have the rows for the
Sales department, you specify which column of data you actually want to extract.
This turns the mini DataFrame into a Pandas Series (just one column of numbers)

"""