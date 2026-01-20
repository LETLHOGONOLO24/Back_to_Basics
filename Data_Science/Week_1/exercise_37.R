# Objective - Mirror Python logic in R
# Tasks
# Load the employees and transactions CSV files
# Replace missing units with department mean
# Compute error rate and efficiency score
# Summarise average efficiency per department

library(dplyr)

# Lets load the data
emp_df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Data_Science/employees_day6.csv')
trans_df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Data_Science/transactions_day6.csv')

# Lets replace missing units
# We use left_join to keep all transactions and bring in employee info
df <- trans_df %>%
  left_join(emp_df, by = "employee_id") %>%
  group_by(department) %>%
  mutate(units_processed = ifelse(is.na(units_processed),
                                  mean(units_processed, na.rm = TRUE),
                                  units_processed)) %>%
  ungroup() # Always ungroup after you are done with group-based math

# Lets compute metrics
df <- df %>%
  mutate(
    error_rate = errors_made / units_processed,
    efficiency_score = units_processed / (errors_made + 1)
  )

# Lets summarise average efficiency per department
dept_summary <- df %>%
  group_by(department) %>%
  summarise(
    avg_efficiency = mean(efficiency_score),
    total_staff = n_distinct(employee_id)
  )

print(dept_summary)

# The mutate() is for creating a new column like df[''] in Python
# Instead of df.groupby().transform(), in R we use df %>% group_by() %>% mutate()

# In R, the mean() function will return NA if there's a single missing value, so
# you must tell R to remove NAs, so na.rm means na.remove
# The first mutate() tells us that if NA is found in units_processed, fill it
# with the mean of units_processed