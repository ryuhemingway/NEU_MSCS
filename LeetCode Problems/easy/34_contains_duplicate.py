"""
Problem 217: Contains Duplicate (Easy)

Given an integer array `nums`, return True if any value appears at least
twice, and False if every element is distinct.

Example:
    Input:  [1, 2, 3, 1]   -> True
    Input:  [1, 2, 3, 4]   -> False

Hint: One-liner with a set is fine, but think about doing it in a single pass
with early exit using a seen-set.
"""


def contains_duplicate(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def contains_duplicate(nums):
#     seen = set()
#     for n in nums:
#         if n in seen:
#             return True
#         seen.add(n)
#     return False
