# R exercise

# Create a variable called ticket_type with one of these values: "technical", "billing", or "feedback"
# Create a variable called customer_tier with one of these values: "premium", "regular", or "new"

# Create a variable called response_time (in hours) with a number between 1-72
# Write if-else statements that determine the priority level ("high", "medium", or "low") based on these rules

# HIGH priority if:
# Ticket is "technical" AND customer is "premium"
# OR response time is less than 4 hours
# OR ticket is "billing" AND amount > $500 (assume a variable billing_amount exists)

# LOW priority if:
# Ticket is "feedback"
# AND customer is not "premium"
# AND response time is greater than 48 hours

# MEDIUM  priority for everything else
# Print the result: "Priority level: [high/medium/low]"

# Lets set up the variables
ticket_type <- "technical"
customer_tier <- "premium"
response_time <- 3
billing_amount <- 600

# Lets initialize priority variable
priority <- ""

if (ticket_type == "technical" & customer_tier == "premium") {
	priority <- "HIGH"
} else if (response_time < 4) {
	priority <- "HIGH"
} else if (ticket_type == "billing" & billing_amount > 500) {
	priority <- "HIGH"
} else if (ticket_type == "feedback" & customer_tier != "premium" & response_time > 48) {
	priority <- "LOW"
} else {
	priority <- "LOW"
}

print(paste("Priority level:", priority))

if (priority == "HIGH" & response_time < 2) {
	print("URGENT - Call customer immediately!")
} else {
  print("RELAX")
}
