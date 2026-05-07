"""
Problem 62: Unique Paths (Medium)

A robot is on an m x n grid, starting at top-left. It can only move right or
down. How many unique paths are there to the bottom-right corner?

Example:
    Input:  m = 3, n = 7   -> 28
    Input:  m = 3, n = 2   -> 3

Hint: dp[i][j] = dp[i-1][j] + dp[i][j-1]. Edges (top row, leftmost col) are
all 1. Can be reduced to a single row of size n.
"""


def unique_paths(m, n):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def unique_paths(m, n):
#     row = [1] * n
#     for _ in range(1, m):
#         for j in range(1, n):
#             row[j] += row[j - 1]
#     return row[-1]
