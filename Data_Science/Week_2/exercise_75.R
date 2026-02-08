# Lets load the data
df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Data_Science/Week_2/performance_day11.csv')

# Lets create the target variable
df$error_rate <- df$errors_made / df$units_processed

# Lets fit the multiple Linear Model
model <- lm(error_rate ~ training_hours + avg_processing_time, data = df)

# Lets view the results
summary(model)