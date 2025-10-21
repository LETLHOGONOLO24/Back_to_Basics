"""

PROBLEM

You are given a sorted list of integers and a target value.
If the target is found in the list, return its index.

If not, return the index where it should be inserted to maintain
the sorted order.

You must use Binary Search to achieve O(log n) time complexity.

Input: nums = [1, 3, 5, 6], target = 5  
Output: 2

Input: nums = [1, 3, 5, 6], target = 2  
Output: 1

Input: nums = [1, 3, 5, 6], target = 7  
Output: 4



STEPS


1 - 




"""

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2 # Find the middle index

        if nums[mid] == target:
            return mid # Target found
        elif nums[mid] < target:
            left = mid + 1 # Move to right half
        else:
            right = mid - 1 # Move to left half

    return left # Position where target should be inserted

print(searchInsert([1,3,5,6], 5))