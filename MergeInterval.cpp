/*



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

        return merged;
    }
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