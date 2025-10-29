"""

PROBLEM


You are given a 2D grid consisting of 1s (land) and 0s (water).
An island is formed by connecting adjacent lands horizontally or
vertically.

Your task is to find the size of the largest island, where the size is
the number of connected land cells.


STEPS


1 - 



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