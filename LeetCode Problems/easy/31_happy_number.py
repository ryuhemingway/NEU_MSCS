"""
Problem 202: Happy Number (Easy)

A number is "happy" if repeatedly replacing it with the sum of squares of its
digits eventually reaches 1. If it loops forever (never reaching 1), it is
not happy. Given an integer `n`, return True if it is happy.

Example:
    Input:  19  -> True   (1^2+9^2=82, 8^2+2^2=68, 6^2+8^2=100, 1+0+0=1)
    Input:  2   -> False

Hint: Use a set to detect a cycle, OR use Floyd's tortoise-and-hare with two
"next number" pointers.
"""


def is_happy(n):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def is_happy(n):
#     def squared_digit_sum(x):
#         total = 0
#         while x:
#             x, d = divmod(x, 10)
#             total += d * d
#         return total
#
#     seen = set()
#     while n != 1 and n not in seen:
#         seen.add(n)
#         n = squared_digit_sum(n)
#     return n == 1
