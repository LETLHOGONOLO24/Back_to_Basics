"""

PROBLEM


You are given a 2D grid consisting of 1s (land) and 0s (water).
An island is formed by connecting adjacent lands horizontally or
vertically.

Your task is to find the size of the largest island, where the size is
the number of connected land cells.


STEPS


1 -  if not grid: Check if input grid is empty
2 - rows, cols = len(grid), len(grid[0]) Get number of rows and columns

3 - visited = set() Create a set to track visited cells and remove duplicates
4 - def dfs(r, c): Define an inner recursive function dfs that will explore
    (mark and traverse) all connected "1" cells starting from (r, c).

    r < 0 or c < 0 or r >= rows or c >= cols: out of grid bounds → stop.
    grid[r][c] == "0": the current cell is water (not part of an island) → stop.

    After starting at the nested loops, the code comes here

    (r, c) in visited: already explored this cell → stop.
    If any of these are true, the function returns without doing anything.

    If this recursion (dfs(r, c) is true, it won't put the cell it visited
    in set and area wont be 1 and it will return 0, but if the if statement
    is false, then the current cell will be in visted and area will be 1)

5 - visited.add((r, c)) - Mark the current cell as visited to avoid
    reprocessing it later (prevents infinite recursion / repeated work).

        # explore neighbors (up, down, left, right)
        area += dfs(r - 1, c)
        area += dfs(r + 1, c)
        area += dfs(r, c - 1)
        area += dfs(r, c + 1)

        Each direction must return area

        Recursively call dfs on the four orthogonal neighbors (4-directional
        flood fill). This explores the whole connected component of "1"s.

6 - max_area = 0 - initialize max_area counter
7 - Nested loops to visit every cell in the grid. (code starts here, r=0, c=0)

8 - if grid[r][c] == "1" and (r, c) not in visited: If the cell is land ("1")
    and hasn't been visited yet, max_area is the maximum between max_area and dfs(r, c)

    max_area = max(max_area, dfs(r, c))
    Start DFS from that cell to mark the entire island as visited, then increment
    the island area by 1 if land is found.



"""

class Solution:
    def maxAreaOfIsland(self, grid: list) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0
            
            visited.add((r,c))
            area = 1

            # Explore 4 directions
            area += dfs(r - 1, c)
            area += dfs(r + 1, c)
            area += dfs(r, c - 1)
            area += dfs(r, c + 1)

            return area
        
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area
    
sol = Solution()
grid = [
[0,0,1,0,0,0,1,1],
[0,1,1,0,0,0,1,0],
[0,0,0,0,1,0,0,0],
[1,1,0,0,1,1,0,0]
]

print(sol.maxAreaOfIsland(grid))