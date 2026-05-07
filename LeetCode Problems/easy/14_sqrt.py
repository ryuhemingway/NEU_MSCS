"""
Problem 69: Sqrt(x) (Easy)

Given a non-negative integer `x`, return the square root rounded down to the
nearest integer. You must not use any built-in exponent or square-root.

Example:
    Input:  x = 4   -> 2
    Input:  x = 8   -> 2  (sqrt(8) ~ 2.828, floored to 2)

Hint: Binary search on the answer in [0, x]. Look for the largest `m` such
that m*m <= x.
"""


def my_sqrt(x):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def my_sqrt(x):
#     if x < 2:
#         return x
#     lo, hi = 1, x // 2
#     ans = 0
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if mid * mid <= x:
#             ans = mid
#             lo = mid + 1
#         else:
#             hi = mid - 1
#     return ans
