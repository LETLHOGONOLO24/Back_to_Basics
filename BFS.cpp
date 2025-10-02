/*

Problem: Shortest path in binary matrix.


STEPS


1 - We include vectors since we're dealing with a grid or NxN matrix
2 - The if statement checks if start or end is blocked meaning it checks
    if the first element and last element in the grid is a 0 or 1 and if
    it is a 1, the program must return -1 because 1 signals a bocked cell

    We return -1 because it says we can't begin moving because of a blocked
    cell (1)

3 - The directions vector stores all possible directions which are 8 (left,
    right, up, down, diagonal left, diagonal right, diagonal up and diagonal
    down). Each pair represents (row_change, column_change_

4 - The queue stores the row, column, distance. Since the first element is
    the start (0, 0), we say its distance = 1

    Visited is a vector matrix with a size n x n to keep track of whether each
    cell has been visited or not and since it says false, each cell hasn't been
    visited

    visited = [
        false, false,
        false, false
    ]

    visited[0][0] = true says the first element has visited the first cell
    visited = [
        true, false,
        false, false
    ]

5 - The while loop only loops when the queue is not empty and since it has
    values of the first element and its distance, its going to loop
    





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