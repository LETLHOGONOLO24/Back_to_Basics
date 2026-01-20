# Objective - Reinforce statistical thinking
# Task
# Load the CSV

# Compute efficiency score
# Rank employees

# Calculate percentiles
# Label performance tiers

library(dplyr)

# Lets load the data
df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Data_Science/Week_1/performance_day7.csv')

# Computing efficiency score and rank
# We use mutate to add columns and desc() to rank from highest to lowest
df <- df %>%
  mutate(
    efficiency_score = units_processed / (errors_made + 1),
    rank = min_rank(desc(efficiency_score))
  )

# Lets calculate percentile thresholds
p25 <- quantile(df$efficiency_score, 0.25)
p75 <- quantile(df$efficiency_score, 0.75)

# Lets label performance tiers
# case_when is the gold standard for labeling in R
df <- df %>%
  mutate(performance_tier = case_when(
    efficiency_score <= p25 ~ "Bottom 25%",
    efficiency_score <= p75 ~ "Top 25%",
    TRUE                    ~ "Middle 50%"
  ))

df_final <- df %>%
  select(employee_name, efficiency_score, rank, performance_tier) %>%
  arrange(rank)

print(df_final)