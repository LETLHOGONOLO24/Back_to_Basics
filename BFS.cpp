/*

Problem: Shortest path in binary matrix.



*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
    public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();

        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;

        vector<pair<int,int>> directions = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
        queue<tuple<int,int,int>> q;
        q.push({0,0,1});
        vector<vector<bool>> visited(n, vector<bool>(n,false));
        visited[0][0] = true;

        while (!q.empty()) {
            auto [r,c,dist] = q.front();
            q.pop();

            if (r == n-1 && c == n-1) return dist;

            for (auto [dr, dc] : directions) {
                int nr = r+dr, nc = c+dc;

                if (nr >= 0 && nc >= 0 && nr < n && nc < n && grid[nr][nc] == 0 && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.push({nr,nc,dist+1});
                }
            }
        }
        return -1;
    }
};

int main() {
    vector<vector<int>> grid = {{0,1},{1,0}};
    Solution s;
    cout << s.shortestPathBinaryMatrix(grid);
    return 0;
}