"""
Problem 35: Search Insert Position (Easy)

Given a sorted array of distinct integers and a target value, return the index
where it would be inserted in order. Must run in O(log n) time.

Example:
    Input:  nums = [1, 3, 5, 6], target = 5  -> 2
    Input:  nums = [1, 3, 5, 6], target = 2  -> 1
    Input:  nums = [1, 3, 5, 6], target = 7  -> 4

Hint: Classic binary search. When the loop ends with lo > hi, lo is exactly
the insertion position.
"""


def search_insert(nums, target):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def search_insert(nums, target):
#     lo, hi = 0, len(nums) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             lo = mid + 1
#         else:
#             hi = mid - 1
#     return lo
