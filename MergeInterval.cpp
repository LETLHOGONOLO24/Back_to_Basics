/*

PROBLEM


You are given an array of intervals where
intervals[i] = [start_i, end_i].

Merge all overlapping intervals and return an array of the non-
overlapping intervals that cover all the intervals in the input.


Example 1:

Input:
intervals = [[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]

Explanation:
Intervals [1,3] and [2,6] overlap → merged into [1,6].

Example 2:

Input:
intervals = [[1,4],[4,5]]

Output:
[[1,5]]

Explanation:
Even though the end of one interval equals the start of another,
they are merged since they touch.

Constraints:

1 <= intervals.length <= 10^4

intervals[i].length == 2

0 <= start_i <= end_i <= 10^4



*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    // Step 1: Sort intervals by start time
    sort(intervals.begin(), intervals.end());

    vector<vector<int>> merged;

    for (auto interval : intervals) {
        if (merged.empty() || merged.back()[1] < interval[0]) {
            merged.push_back(interval);
        }
        else {
            merged.back()[1] = max(merged.back()[1], interval[1]);
        }
    }
     return merged;
}

int main() {
    vector<vector<int>> intervals = {{1,3},{2,6},{8,10},{15,18}};

    vector<vector<int>> result = merge(intervals);

    cout << "Merged intervals: ";
    for (auto interval : result) {
        cout << "[" << interval[0] << "," << interval[1] << "] ";
    }
    cout << endl;

    return 0;
}