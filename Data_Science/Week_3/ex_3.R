df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Data_Science/Week_3/sales.csv')

# Ensure the sale_date column is treated as a Date object
sales$sale_date <- as.Date(sales$sale_date)

# 2. Filter transactions where quantity > 3 AND price > 800
high_value_sales <- sales[sales$quantity > 3 & sales$price > 800, ]

# 3. Filter transactions between specific dates (Example: Q1 2024)
start_date <- as.Date("2024-01-01")
end_date <- as.Date("2024-03-31")
date_filtered_sales <- sales[sales$sale_date >= start_date & sales$sale_date <= end_date, ]

# 4. Find all transactions for product_id 2
product_2_sales <- sales[sales$product_id == 2, ]

# View the results
print(head(high_value_sales))
print(nrow(date_filtered_sales))
print(product_2_sales)