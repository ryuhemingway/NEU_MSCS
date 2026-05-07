"""
Problem 169: Majority Element (Easy)

Given an array `nums` of size n, return the majority element -- the one that
appears more than n//2 times. You may assume one always exists.

Example:
    Input:  [3, 2, 3]               -> 3
    Input:  [2, 2, 1, 1, 1, 2, 2]   -> 2

Hint: Boyer-Moore voting -- maintain a candidate and a count. Same value
increments count; different decrements; when count hits 0 pick a new
candidate. O(n) time, O(1) space.
"""


def majority_element(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def majority_element(nums):
#     count = 0
#     candidate = None
#     for n in nums:
#         if count == 0:
#             candidate = n
#         count += 1 if n == candidate else -1
#     return candidate
