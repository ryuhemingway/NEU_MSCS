"""
Problem 231: Power of Two (Easy)

Given an integer `n`, return True if it is a power of two; otherwise False.
A power of two is any number of the form 2^k for some integer k >= 0.

Example:
    Input:  1   -> True   (2^0)
    Input:  16  -> True   (2^4)
    Input:  3   -> False

Hint: Powers of two have exactly one bit set in binary. Trick: n > 0 and
(n & (n - 1)) == 0.
"""


def is_power_of_two(n):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def is_power_of_two(n):
#     return n > 0 and (n & (n - 1)) == 0
