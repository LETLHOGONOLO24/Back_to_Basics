"""

Problem: Find the maximum sum of any contiguous subarray of size k.
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9 (subarray [5,1,3])


STEPS


1 - max_sum = float('-inf')  # Tracks maximum sum found (start with
    negative infinity)
2 - for window_end in range(len(arr)): Loop through array with window
    _end as the end of our sliding window

3 - window_sum += arr[window_end] - Add the new element that just
    entered the window
4 - if window_end >= k - 1: Check if we've reached the required
    window size (k). We need k-1 because indices are 0-based

5 - max_sum = max(max_sum, window_sum) - Update max_sum if current
    window sum is larger
6 - window_sum -= arr[window_start] - Remove the element that's leaving
    the window

7 - window_start += 1 - Move the start of the window forward


"""

def max_sum_subarray(arr, k):
    window_sum = 0
    max_sum = float('-inf')
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end] # add next element

        # When window size reaches k, calculate sum
        if window_end >= k -1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start] # removes first element
            window_start += 1 # slide window ahead

    return max_sum

print(max_subarray_sum([2,1,5,1,3,2], 3))