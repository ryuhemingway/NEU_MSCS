"""
Problem 268: Missing Number (Easy)

Given an array `nums` containing n distinct numbers in [0, n], return the one
number that is missing from the range.

Example:
    Input:  [3, 0, 1]               -> 2
    Input:  [0, 1]                  -> 2
    Input:  [9, 6, 4, 2, 3, 5, 7, 0, 1] -> 8

Hint: Two clean approaches: (a) sum 0..n minus sum(nums); (b) XOR all
indices 0..n with all values, the one missing survives.
"""


def missing_number(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def missing_number(nums):
#     n = len(nums)
#     return n * (n + 1) // 2 - sum(nums)
