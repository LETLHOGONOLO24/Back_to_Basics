"""

PROBLEM

You are climbing a staircase. It takes n steps to reach the top.
Each time, you can either climb 1 step or 2 steps.
In how many distinct ways can you climb to the top?


STEPS


1 - If n is 1 or 2 (or 0), return n immediately.
    - For n = 1, there is 1 way: [1].

    - For n = 2, there are 2 ways: [1+1] and [2].
    - Note: with this code n = 0 returns 0. (Some definitions count
    n=0 as 1 way — “do nothing”. This implementation treats it as 0.)

2 - dp = [0] * (n + 1) Create a list dp of length n+1, initialized with
    zeros.
    - We use indices 0..n. Index i corresponds to number of ways to reach
    step i.

    - dp[0] is unused (kept 0 here), dp[1] is ways to reach step 1, etc.
3 - dp[1], dp[2] = 1, 2 # base cases

    - Initialize the known base values: dp[1] = 1 (one way to reach step 1)
    dp[2] = 2 (two ways to reach step 2)
    These are the seeds for building larger dp values.

4 - for i in range(3, n + 1): For each step i from 3 to n, compute dp[i] as
    sum of:
    - dp[i-1] — ways to reach i-1, then take one step → reach i

    - dp[i-2] — ways to reach i-2, then take two steps → reach i
    - This is the recurrence: ways(i) = ways(i-1) + ways(i-2) (same as Fibonacci)

5 - return dp[n] Return the computed number of ways to reach step n.


SIMULATION


Initial: n = 5 → n > 2, so we build dp.
dp = [0, 0, 0, 0, 0, 0] (indexes 0..5)

dp[1] = 1, dp[2] = 2
dp = [0, 1, 2, 0, 0, 0]

Now loop i = 3..5:
    i = 3: dp[3] = dp[2] + dp[1] = 2 + 1 = 3
    dp = [0, 1, 2, 3, 0, 0]

    i = 4: dp[4] = dp[3] + dp[2] = 3 + 2 = 5
    dp = [0, 1, 2, 3, 5, 0]

    i = 5: dp[5] = dp[4] + dp[3] = 5 + 3 = 8
    dp = [0, 1, 2, 3, 5, 8]

Loop ends → return dp[5] = 8.
So print(climbStairs(5)) prints: 8



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