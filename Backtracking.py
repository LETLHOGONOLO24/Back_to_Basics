"""

PROBLEM

Given an array of unique integers nums, return all possible subsets
(the power set).
The solution set must not contain duplicates, and you may return the
subsets in any order.


STEPS




"""

def subsets(nums):
    result = []
    current = []

    def backtrack(index):
        result.append(list(current)) # add a copy of current subset
        for i in range(index, len(nums)):
            current.append(nums[i]):
            backtrack(i + 1)
            current.pop()

    backtrack(0)
    return result

print(subsets([1,2,3]))