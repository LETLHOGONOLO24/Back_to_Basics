library(dplyr)

# Lets load the CSV
df <- read.csv('C:/Users/HLOGIZNBUCKS/Downloads/Back_to_Basics/Data_Science/Week_2/performance_day8.csv')

# Lets create features by calculating error_rate and speed_score (1 / time)
df <- df %>%
  mutate(
    error_rate = errors_made / units_processed,
    speed_score = 1 / avg_processing_time
  )

# Lets normalize features (Min-Max Scaling)
# We create a helper function to keep the code clean
min_max <- function(x) { (x - min(x)) / (max(x) - min(x)) }

df <- df %>%
  mutate(
    u_norm = min_max(units_processed),
    s_norm = min_max(speed_score),
    e_norm = min_max(error_rate)
  )

# Lets compute composite score
# Weights: 0.5 (Units), 0.3 (Speed), 0.2 (Quality/1 - Errors)
df <- df %>%
  mutate(
    composite_score = (0.5 * u_norm) + (0.3 * s_norm) * (0.2 * (1 - e_norm))
  )

# Lets rank employees
df <- df %>%
  mutate(rank = min_rank(desc(composite_score))) %>%
  arrange(rank)

# Lets view final results
print(df %>% select(employee_name, department, composite_score, rank))