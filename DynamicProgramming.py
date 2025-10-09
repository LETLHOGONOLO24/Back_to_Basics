"""

PROBLEM

You are climbing a staircase. It takes n steps to reach the top.
Each time, you can either climb 1 step or 2 steps.
In how many distinct ways can you climb to the top?


STEPS




"""

def climbStairs(n):
    # Base case
    if n <= 2:
        return n
    
    # dp[i] will hold the number of ways to reach step i
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2 # base cases

    # Build up from step 3 to n
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] # Previous two steps

    return dp[n]

print(climbStairs(5))