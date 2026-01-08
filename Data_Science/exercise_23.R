# Objective - Mirror Python logic in R
# Tasks
# -Load the CSV
# Compute Revenue
# Aggregate daily revenue
# Calculate a 3-day rolling mean

library(zoo)

# Lets load the data
df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Data_Science/sales_day4.csv')

# lets compute revenue
df$revenue <- df$units_sold * df$price

# Aggregate daily revenue
daily_revenue <- aggregate(revenue ~ date, df, sum) # Split the revenue column by date from df and sum the revenue

# Calculate a 3-day rolling mean
# k = 3 defines the window size
# fill = NA keeps the table the same length by putting NAs in the first two rows
daily_revenue$moving_avg <- rollmean(daily_revenue$revenue, k = 3, fill = NA, align = "right")

print(daily_revenue)