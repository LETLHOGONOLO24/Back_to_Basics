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

    auto [r,c,dist]: C++17 structured binding to unpack tuple. Basically, 
    q.front() is retrieving the tuple (0, 0, 1). This line of code says this
    tuple should be at the front or it is the first element in the queue (oldest
    one inserted)

    Once we process that element (unpack r, c, dist and maybe expand neighbors),
    it’s no longer needed. So, q.pop() → removes that front element from the queue.
    If you don’t pop, then q.front() would always give you the same element again
    and again like an infinite loop.

6 - The if statement says If we reached destination (bottom-right), return current
    distance

7 - The for loop says delta row and delta column are our indices in directions. 
    new row adds the row recorded in the queue with the index dr, same with new column
    
    New row and new column should be less than 2 so that they are not out of bounds
    Both nr and nc should be 1, they musn't alternate because the program might check
    blocked cell

    grid[nr][nc] == 0 means it must be on a zero in the grid and visited must be
    false meaning it hasnt visited this zero. If all the conditions are true, 

    visited[nr][nc] = true; mark this cell as visited and q.push({nr, nc, dist+1});
    push these tuples in the queue while increasing the distance by 1

    IN SHORT, THE IF STATEMENT WILL CHECK THE NEXT ROW, SAME COLUMN BECAUSE IT CHECKS
    THE SHORTEST PATH

8 - Return -1 if no path is found





*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
    public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();

        // Edge case, check whether we're not checking on a blocked cell
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