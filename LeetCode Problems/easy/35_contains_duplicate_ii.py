"""
Problem 219: Contains Duplicate II (Easy)

Given an integer array `nums` and an integer `k`, return True if there are
two distinct indices i, j such that nums[i] == nums[j] and abs(i - j) <= k.

Example:
    Input:  nums = [1,2,3,1], k = 3       -> True
    Input:  nums = [1,2,3,1,2,3], k = 2   -> False

Hint: Hash map of value -> latest index. While walking, check if a previous
index is within k.
"""


def contains_nearby_duplicate(nums, k):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def contains_nearby_duplicate(nums, k):
#     last = {}
#     for i, n in enumerate(nums):
#         if n in last and i - last[n] <= k:
#             return True
#         last[n] = i
#     return False
