# Lets load the data
df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Data_Science/Week_2/performance_day10.csv')

# 2. Extract processing times for both departments
sales <- df$avg_processing_time[df$department == "Sales"]
ops <- df$avg_processing_time[df$department == "Operations"]

# 3. Compute Confidence Intervals using t.test
# We run a t.test for each group to get their specific CIs
sales_stats <- t.test(sales)
ops_stats <- t.test(ops)

# 4. Compute Cohen’s d (requires 'effsize' library or manual math)
# Manual math for Cohen's d:
pooled_sd <- sqrt(((length(sales)-1)*var(sales) + (length(ops)-1)*var(ops)) / (length(sales)+length(ops)-2))
cohens_d <- (mean(sales) - mean(ops)) / pooled_sd

# 5. Print Results
cat("Sales 95% CI:", sales_stats$conf.int, "\n")
cat("Operations 95% CI:", ops_stats$conf.int, "\n")
cat("Cohen's d:", cohens_d, "\n")