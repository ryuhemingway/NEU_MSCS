"""
Problem 200: Number of Islands (Medium)

Given an m x n 2D grid of '1's (land) and '0's (water), return the number of
islands. An island is surrounded by water and formed by horizontally or
vertically adjacent lands.

Example:
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]   -> 1

    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]   -> 3

Hint: DFS or BFS from each unvisited '1', sinking the whole island. Each new
DFS launch counts as one island.
"""


def num_islands(grid):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def num_islands(grid):
#     if not grid:
#         return 0
#     rows, cols = len(grid), len(grid[0])
#     def dfs(r, c):
#         if (r < 0 or r >= rows or c < 0 or c >= cols
#                 or grid[r][c] != '1'):
#             return
#         grid[r][c] = '0'
#         dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
#
#     count = 0
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == '1':
#                 dfs(r, c)
#                 count += 1
#     return count
