"""

Problem: Count the number of islands in a grid (1 = land, 0 = water).


STEPS


1 -  if not grid: Check if input grid is empty
2 - rows, cols = len(grid), len(grid[0]) Get number of rows and columns

3 - visited = set() Create a set to track visited cells and remove duplicates
4 - def dfs(r, c): Define an inner recursive function dfs that will explore
    (mark and traverse) all connected "1" cells starting from (r, c).

    r < 0 or c < 0 or r >= rows or c >= cols: out of grid bounds → stop.
    grid[r][c] == "0": the current cell is water (not part of an island) → stop.

    (r, c) in visited: already explored this cell → stop.
    If any of these are true, the function returns without doing anything.

5 - visited.add((r, c)) - Mark the current cell as visited to avoid
    reprocessing it later (prevents infinite recursion / repeated work).

        # explore neighbors (up, down, left, right)
        dfs(r+1, c) # Down
        dfs(r-1, c) # Up
        dfs(r, c+1) # Right
        dfs(r, c-1) # Left

        Recursively call dfs on the four orthogonal neighbors (4-directional
        flood fill). This explores the whole connected component of "1"s.

6 - count = 0 - initialize island counter
7 - Nested loops to visit every cell in the grid.

8 - if grid[r][c] == "1" and (r, c) not in visited: If the cell is land ("1")
    and hasn't been visited yet, it marks the start of a new island.

    dfs(r, c)
    count += 1
    Start DFS from that cell to mark the entire island as visited, then increment
    the island count by 1.






"""

def numIslands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):

        # return if out of bounds or water or already visited
        if (r < 0 or c < 0 or r >= rows or c >= cols or
            grid[r][c] == "0" or (r, c) in visited):
            return
        visited.add((r, c))

        # explore neighbors (up, down, left, right)
        dfs(r+1, c) # Down
        dfs(r-1, c) # Up
        dfs(r, c+1) # Right
        dfs(r, c-1) # Left

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count

print(numIslands([
    ["1","1","0","0"],
    ["1","0","0","1"],
    ["0","0","1","1"],
    ["0","0","0","0"]
]))