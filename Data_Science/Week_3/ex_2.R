library(dplyr)

# Lets load the data
df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Data_Science/Week_3/sales.csv')

# Lets inspect the structure
head(df)
tail(df)
View(df)

# Lets create a new column called total transaction value
df <- df %>%
  mutate(
    total_transaction_value = quantity * price
  )
print(df)

# Lets create price squared and quantity cubed
df <- df %>%
  mutate(
    price_squared = price^2,
    quantity_cubed = quantity^3
  )
print(df)

# Lets calculate square root of price, natural log of price and exponential of quantity
df <- df %>%
  mutate(
    sqrt_price = sqrt(price),
    natural_log_price = log(price),
    exp_quantity = exp(quantity)
  )
print(df)

# Lets find the mean, max and min of transaction value
df <- df %>%
  mutate(
    mean_tv = mean(price * quantity),
    max_tv = max(price * quantity),
    min_tv = min(price * quantity)
  )
print(df)

