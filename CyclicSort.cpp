/*


PROBLEM


Given an array containing n distinct numbers taken from the range 0 to
n, find the one number that is missing from the array.

Input: [4, 0, 2, 1]
Output: 3
Explanation: All numbers from 0 to 4 are expected → 3 is missing.



STEPS


1 - while (i < n) { We loop through each index until we reach the end.
2 - int correctIndex = nums[i]; Each number x should ideally be at
    index x. So correctIndex is where the current number should go.

3 - if (nums[i] < n && nums[i] != nums[correctIndex]) {
    swap(nums[i], nums[correctIndex]);
    } 

    We only swap when:
    - The number is within range (less than n), and
    - It is not already in the correct position.
    - If both are true → swap to move it to its correct index.

4 - If the number is already in the correct position (or invalid),
    move to the next index.



*/

#include <iostream>
#include <vector>
using namespace std;

int missingNumber(vector<int>& nums) {
    int i = 0;
    int n = nums.size();

    while (i < n) {
        int correctIndex = nums[i];
        if (nums[i] < n && nums[i] != nums[correctIndex]) {
            swap(nums[i], nums[correctIndex]);
        }
        else {
            i++;
        }
    }

    for (int i = 0; i < n; i++) {
        if (nums[i] != 1) {
            return i;
        }
    }

    return n;
}

int main() {
    vector<int> nums = {4, 0, 2, 1};
    cout << "Missing number: " << missingNumber(nums) << endl;
    return 0;
}