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


1 - left, right = 0, len(nums) - 1: left starts from the first index
    (0). right starts from the last index (len(nums) - 1).

2 - while left <= right: The loop continues as long as there's a valid
    search space.
3 - mid = (left + right) // 2: The // ensures integer division. The
    middle helps us decide which half to continue searching.

4 - if nums[mid] == target: return mid -> If the element at mid equals
    target, we return mid immediately
5 - elif nums[mid] < target: left = mid + 1 -> Since the list is sorted,
    if the middle element is smaller than the target, the target must
    be in the right half.

6 - else: right = mid - 1 -> If the middle element is greater, move the
    search to the left half.
7 - When the loop ends, left is the position where the target should be
    inserted to keep the list sorted.




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