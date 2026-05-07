"""
Problem 33: Search in Rotated Sorted Array (Medium)

A sorted-ascending array of distinct integers was rotated at some unknown
pivot. Given the rotated array `nums` and an integer `target`, return the
target's index, or -1. Must run in O(log n).

Example:
    Input:  nums = [4,5,6,7,0,1,2], target = 0   -> 4
    Input:  nums = [4,5,6,7,0,1,2], target = 3   -> -1

Hint: Modified binary search. At each mid, exactly one half is properly
sorted -- check which, then decide whether target lies in that half.
"""


def search(nums, target):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def search(nums, target):
#     lo, hi = 0, len(nums) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if nums[mid] == target:
#             return mid
#         if nums[lo] <= nums[mid]:               # left half sorted
#             if nums[lo] <= target < nums[mid]:
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#         else:                                   # right half sorted
#             if nums[mid] < target <= nums[hi]:
#                 lo = mid + 1
#             else:
#                 hi = mid - 1
#     return -1
