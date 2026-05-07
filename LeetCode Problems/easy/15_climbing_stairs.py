"""
Problem 70: Climbing Stairs (Easy)

You are climbing a staircase of `n` steps. Each step you can climb 1 or 2
steps. In how many distinct ways can you reach the top?

Example:
    Input:  n = 2   -> 2     (1+1, or 2)
    Input:  n = 3   -> 3     (1+1+1, 1+2, 2+1)

Hint: ways(n) = ways(n-1) + ways(n-2) -- it's just Fibonacci. Iterative DP
with two variables is O(n) time, O(1) space.
"""


def climb_stairs(n):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def climb_stairs(n):
#     if n <= 2:
#         return n
#     a, b = 1, 2
#     for _ in range(3, n + 1):
#         a, b = b, a + b
#     return b
