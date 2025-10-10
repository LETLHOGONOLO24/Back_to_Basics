"""

PROBLEM

Given an array of unique integers nums, return all possible subsets
(the power set).
The solution set must not contain duplicates, and you may return the
subsets in any order.


STEPS


1 - result = [] Create an empty list result that will collect all
    subsets. Each element of result is itself a list (a subset).
2 - current = [] holds the subset being built at the current point in
    recursion (the partial solution). It changes as we choose/unchoose
    elements.

3 - def backtrack(index) Define an inner recursive function backtrack
    which explores all subsets that can be built starting from position
    index in nums.

4 - result.append(list(current)) Append a copy of current to result
     - list(current) makes a shallow copy so later changes to current do
     not mutate the stored subset.

     - This line records the current subset (including the empty subset at
     the start).
5 - for loop Loop over all choices for the next element to include, starting
    at index. This enforces that we only consider later elements, preventing
    duplicates and preserving order (so subsets like [2,1] won't be produced
    separately from [1,2]).

6 - current.append(nums[i]) Choose nums[i]: add it to the current subset.
7 - backtrack(i + 1) Recurse to explore all subsets that include the chosen
    element nums[i]. Passing i+1 ensures the next recursion only considers
    elements after i.

8 - current.pop() Undo the previous choice (backtrack). Remove the last element
    so we can try the next i in the loop with current restored to its previous state.
9 - backtrack(0) Start the recursion at index 0. This begins exploring all subsets built
    from the entire list.

10 - return result After recursion finishes, return the collected list of all subsets.
    


"""

def subsets(nums):
    result = []
    current = []

    def backtrack(index):
        result.append(list(current)) # add a copy of current subset
        for i in range(index, len(nums)):
            current.append(nums[i])
            backtrack(i + 1)
            current.pop()

    backtrack(0)
    return result

print(subsets([1,2,3]))