"""
Problem 34: Find First and Last Position of Element in Sorted Array (Medium)

Given a sorted array `nums` and a target, find the first and last position of
target in the array. Return [-1, -1] if not found. Must run in O(log n).

Example:
    Input:  nums = [5,7,7,8,8,10], target = 8   -> [3, 4]
    Input:  nums = [5,7,7,8,8,10], target = 6   -> [-1, -1]

Hint: Two binary searches -- one for leftmost target index, one for rightmost.
Or use bisect_left and bisect_right.
"""


def search_range(nums, target):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def search_range(nums, target):
#     def find_left():
#         lo, hi = 0, len(nums) - 1
#         res = -1
#         while lo <= hi:
#             mid = (lo + hi) // 2
#             if nums[mid] >= target:
#                 if nums[mid] == target:
#                     res = mid
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#         return res
#
#     def find_right():
#         lo, hi = 0, len(nums) - 1
#         res = -1
#         while lo <= hi:
#             mid = (lo + hi) // 2
#             if nums[mid] <= target:
#                 if nums[mid] == target:
#                     res = mid
#                 lo = mid + 1
#             else:
#                 hi = mid - 1
#         return res
#
#     return [find_left(), find_right()]
