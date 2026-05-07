"""
Problem 53: Maximum Subarray (Medium)

Given an integer array `nums`, find the contiguous subarray (containing at
least one number) which has the largest sum, and return its sum.

Example:
    Input:  [-2,1,-3,4,-1,2,1,-5,4]   -> 6   (subarray [4,-1,2,1])

Hint: Kadane's algorithm. At each i, current = max(nums[i], current + nums[i]).
Track the best so far. O(n), O(1).
"""


def max_subarray(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def max_subarray(nums):
#     curr = best = nums[0]
#     for n in nums[1:]:
#         curr = max(n, curr + n)
#         best = max(best, curr)
#     return best
