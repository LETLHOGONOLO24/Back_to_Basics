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


1 - 



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