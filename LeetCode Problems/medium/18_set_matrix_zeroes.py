"""
Problem 73: Set Matrix Zeroes (Medium)

Given an m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in-place. Try to use O(1) extra space.

Example:
    Input:  [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Hint: Use the first row and first column as flags themselves. Two booleans
remember whether row 0 / col 0 originally contained a zero. Pass 1 marks
flags; pass 2 zeros out cells; finally handle row 0 / col 0.
"""


def set_zeroes(matrix):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def set_zeroes(matrix):
#     m, n = len(matrix), len(matrix[0])
#     first_row_zero = any(matrix[0][j] == 0 for j in range(n))
#     first_col_zero = any(matrix[i][0] == 0 for i in range(m))
#     for i in range(1, m):
#         for j in range(1, n):
#             if matrix[i][j] == 0:
#                 matrix[i][0] = 0
#                 matrix[0][j] = 0
#     for i in range(1, m):
#         for j in range(1, n):
#             if matrix[i][0] == 0 or matrix[0][j] == 0:
#                 matrix[i][j] = 0
#     if first_row_zero:
#         for j in range(n):
#             matrix[0][j] = 0
#     if first_col_zero:
#         for i in range(m):
#             matrix[i][0] = 0
