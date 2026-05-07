"""
Problem 66: Plus One (Easy)

You are given a non-empty array `digits` where digits[0] is the most-significant
digit of a non-negative integer. Add one to the integer and return the result
as an array of digits.

Example:
    Input:  [1, 2, 3]   -> [1, 2, 4]
    Input:  [9, 9, 9]   -> [1, 0, 0, 0]

Hint: Walk from the right, propagate carry. If you exit the loop with a carry,
prepend a 1.
"""


def plus_one(digits):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def plus_one(digits):
#     for i in range(len(digits) - 1, -1, -1):
#         if digits[i] < 9:
#             digits[i] += 1
#             return digits
#         digits[i] = 0
#     return [1] + digits
