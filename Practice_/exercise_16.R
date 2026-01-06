# 1.Read the CSV file
df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Practice_/sales_day3.csv')

# 2.Convert date to Date type
df$date <- as.Date(df$date)

# 3.Handle missing units_sold by replacing with category mean
# First, calculate means by category
category_means <- aggregate(units_sold ~ category, df, mean, na.rm = TRUE)

# Replace NAs with category means
for(i in 1:nrow(df)) {
  if(is.na(df$units_sold[i])) {
    cat <- df$category[i]
    df$units_sold[i] <- category_means$units_sold[category_means$category == cat]
  }
}

# 4.Compute total revenue per category
df$revenue <- df$units_sold * df$price

# Get total revenue per category
total_revenue_per_category <- aggregate(revenue ~ category, df, sum)

# View results
print(total_revenue_per_category)