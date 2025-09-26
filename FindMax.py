"""

Find the maximum element in a list with exception handling for empty
list.


STEPS


1 - Declare function that takes an array as a parameter
2 - Check if the array is empty or not. If empty, return a ValueError

3 - Declare max_val as 1st element in array
4 - loop through the array

5 - Check if an element is > than the max value. If true, set that element
    to max_value. For loops in python have an increment statement or they
    increment automatically

6 - At the end of the loop, return max_val
7 - Use the try/except statement by trying out the array on the find_max
    function
 8 - Except an error like the one in the 1st if statement



"""

def find_max(arr):
    if not arr:
        raise ValueError("List is empty!")
    
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        return max_val
    
try:
    numbers = [4, 7, 1, 9, 3]
    print("Maximum:", find_max(numbers))
except ValueError as e:
    print(e)