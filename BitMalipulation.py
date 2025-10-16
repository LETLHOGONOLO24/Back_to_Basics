"""


PROBLEM


Given a non-empty array of integers nums, every element appears twice
except for one.
Find that single unique number.

You must implement a solution with O(n) time complexity and O(1) extra
space.


STEPS


1 - The XOR operator (^) has three important properties:

a ^ a = 0 (A number XOR itself is zero)

a ^ 0 = a (A number XOR zero is itself)

a ^ b ^ a = b (Order doesn’t matter — XOR is commutative and
associative)

So if you XOR all numbers together, duplicate numbers cancel out,
and the result is the single unique number.

2 - result = 0 We start with result = 0 because XOR with zero doesn't
    change the value.
3 - for num in nums:
        result ^= num We iterate through the list, XORing each number
        with result.
        Each pair of identical numbers cancels out (since a ^ a = 0),
        leaving only the single number that appears once.







"""

def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num  # XOR all elements

    return result

# Example test
print(singleNumber([4, 1, 2, 1, 2]))
