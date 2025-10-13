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



STEPS


1 - #include <algorithm> – To use sort()
2 - vector<vector<int>> merge(vector<vector<int>>& intervals) Defines
    a function merge that takes a reference to a 2D vector intervals
    and returns a merged version.

3 - sort(intervals.begin(), intervals.end()); Sort intervals by their
    start time (the first element of each pair). Since intervals are
    vectors themselves, sort() will automatically sort by the first
    element, then by second if equal.

4 - vector<vector<int>> merged; Create an empty vector to store merged
    intervals.
5 - if (merged.empty() || merged.back()[1] < interval[0]):

    - merged.empty(): if this is the first interval.
    - merged.back()[1] < interval[0]: if the end of the last merged
    interval is less than the start of the current interval, then
    there’s no overlap.

    - If either condition is true → just push it.
6 - merged.back()[1] = max(merged.back()[1], interval[1]); If overlapping,
    update the end of the last merged interval to the maximum end between
    the two overlapping ones.
    - This merges them into one combined interval.








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