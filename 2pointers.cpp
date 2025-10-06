/*

PROBLEM: Container with Most Water

You are given an array of integers height where each element represents
the height of a vertical line. Find two lines that together with the
x-axis form a container that holds the most water.

Return the maximum amount of water the container can store.

EXAMPLE

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines at indices 1 and 8 (height[1]=8,
height[8]=7) form a container with area = 7 * (8-1) = 49


STEPS


1 - #include <algorithm> — provides min() and max() functions used
    later.
2 - int left = 0; Initialize left pointer to the first index (leftmost
    line).

3 - int right = height.size() - 1; Initialize right pointer to the
    last index (rightmost line).
4 - int max_water = 0; Store the best (maximum) area seen so far.
    Start at 0.

5 - while (left < right) { Loop while there are at least two different
    lines to consider. (When left == right there is no width, so no
    area.)

6 - Compute the area formed by the two lines at indices left and right:
    - min(height[left], height[right]) = effective height of the water

    - (right - left) = width (distance between the two vertical lines).
    - Multiply them to get the area (volume of water in that container
    shape).

    - max_water = max(max_water, current_water); Update max_water to
    the larger of the previous best and current_water.
    - if (height[left] < height[right]) { left++; } else { right--; }
    Move the pointer at the shorter line inward - The goal is to potentially
    find a taller limiting line so that min(...) can increase and maybe produce
    a larger area despite the smaller width.

    - return max_water; When the loop finishes, return the maximum area found.

7 - current_water is the area formed by the two lines at indices left and right.
    It equals:

    current_water = (height of water) * (width between lines)
    = min(height[left], height[right]) * (right - left)

    - Height of water: determined by the shorter of the two lines; taller side
    can’t hold extra water beyond the shorter side.
    - Width: number of units between the two lines (index distance).

    - So current_water is the amount of water that would be contained between
    these two vertical lines.
    - Why min(height[left], height[right])? Because water between two vertical
    lines can only be as tall as the shorter line because if water was as tall
    as the tall line, water would spill over the shorter line. So the height of
    the water is the height of the shorter line

    - If left is 8 and right is 7, the water height is 7, not 8. So min() gives
    the limiting height.
    - Why multiply by (right - left)? (right - left) is the horizontal distance
    between the two lines; it’s the width of the container. Area of a rectangle =
    height × width. Here the container (water region) is height min(...) and width
    right-left. We use subtraction because indices are line positions on the x-axis.

8 - Why max(max_water, current_water)? max_water tracks the best (largest) area seen
    so far. Each pair (left, right) yields a candidate area (current_water). We take
    the larger of the previous best and the candidate so that, by the end of the loop,
    max_water holds the maximum area found across all considered pairs.

9 - Why move the pointer at the shorter line? (the if/else logic) - This is the key
    optimization. The loop moves pointers inward to consider other pairs — but which
    pointer should move?

    - Suppose height[left] < height[right]. The current area is:
    A = height[left] * (right - left)

    - If we keep left fixed and move right leftwards to some new right', the width
    decreases (since right' < right) and the height of the new container becomes
    min(height[left], height[right']). Because height[left] is already smaller than
    height[right], the new min can never be greater than height[left] unless we change
    the left side to something taller. So any area we get by moving the right pointer
    inward will be ≤ height[left] * (right - left') which is strictly less than or equal
    to the current area (width decreased). Thus moving the right pointer cannot produce
    a larger area than A in this situation.

    - Therefore we move left (the shorter one) inward hoping to find a taller line on the
    left side; that could increase the min(...) sufficiently to overcome the loss of width
    and produce a larger area.

    - Symmetrically, if height[right] <= height[left], we move right--.
    - Simple intuition: the max area is constrained by the shorter side; to have any chance
    of increasing area you must try to increase the shorter side — hence move the pointer at
    the shorter side.



*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxArea(vector<int>& height) {
    int left = 0;
    int right = height.size() - 1;
    int max_water = 0;

    while (left < right) {
        int current_water = min(height[left], height[right]) * (right - left);
        max_water = max(max_water, current_water);

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return max_water;
}

int main() {
    vector<int> height = {1,8,6,2,5,4,8,3,7};
    cout << "Maximum water: " << maxArea(height) << endl;

    vector<int> height2 = {1,1};
    cout << "Maximum water: " << maxArea(height2) << endl;

    return 0;
}