"""
Problem 118: Pascal's Triangle (Easy)

Given an integer `numRows`, return the first `numRows` of Pascal's triangle.
Each number is the sum of the two directly above it.

Example:
    Input:  numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Hint: Build each row from the previous: new_row[i] = prev[i-1] + prev[i],
with 1s on each end.
"""


def generate(num_rows):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def generate(num_rows):
#     triangle = []
#     for r in range(num_rows):
#         row = [1] * (r + 1)
#         for i in range(1, r):
#             row[i] = triangle[r - 1][i - 1] + triangle[r - 1][i]
#         triangle.append(row)
#     return triangle
