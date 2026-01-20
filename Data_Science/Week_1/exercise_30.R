# Objective - Mirror Python logic in R
# Tasks
# -Load the CSV
# Compute Revenue
# Calculate correlation between marketing spend and revenue
# Create a scatter plot with a regression line

# Lets load the data
df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Data_Science/sales_day5.csv')

# Lets compute revenue
df$revenue <- df$units_sold * df$price

# Lets calculate correlation between marketing spend and revenue
marketing_revenue_corr <- cor(df$marketing_spend, df$revenue)
print(paste("Correlation:", marketing_revenue_corr))

# Creating a scatter plot with a regression line
# The plot function uses the formula: X ~ Y

plot(df$marketing_spend, df$revenue,
     main = "Marketing Spend vs Revenue",
     xlab = "Marketing Spend (Rand)",
     ylab = "Revenue (Rand)",
     pch = 19, col = "blue") # pch tells R to use solid circles

# Add the regression (trend) line
# lm() creates the Linear Model, abline() draws it
abline(lm(revenue ~ marketing_spend, data = df), col = "red", lwd = 2)