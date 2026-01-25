# Lets load the data
df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Data_Science/Week_2/performance_day9.csv')

# Lets split the data
# We create two vectors of processing time
sales_times <- df$avg_processing_time[df$department == "Sales"]
ops_times <- df$avg_processing_time[df$department == "Operations"]

# Perform the T-Test
#This compares the means of the two groups
results <- t.test(sales_times, ops_times)

# Lets view the results
print(results)