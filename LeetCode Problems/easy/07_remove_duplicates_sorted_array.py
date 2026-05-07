"""
Problem 26: Remove Duplicates from Sorted Array (Easy)

Given a sorted array `nums`, remove the duplicates in-place such that each
unique element appears only once. Return the number of unique elements `k`.
The first `k` slots of `nums` should hold the unique values.

Example:
    Input:  nums = [1, 1, 2]
    Output: 2, nums starts with [1, 2, ...]

    Input:  nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums starts with [0,1,2,3,4, ...]

Hint: Two pointers -- a write pointer that only advances when the current
value differs from the previous kept one.
"""


def remove_duplicates(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def remove_duplicates(nums):
#     if not nums:
#         return 0
#     write = 1
#     for read in range(1, len(nums)):
#         if nums[read] != nums[read - 1]:
#             nums[write] = nums[read]
#             write += 1
#     return write
