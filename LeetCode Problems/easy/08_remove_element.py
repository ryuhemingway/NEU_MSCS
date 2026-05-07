"""
Problem 27: Remove Element (Easy)

Given an integer array `nums` and an integer `val`, remove all occurrences of
`val` in-place. The order of remaining elements may be changed. Return the new
count `k`; the first `k` slots of `nums` should hold the kept elements.

Example:
    Input:  nums = [3, 2, 2, 3], val = 3
    Output: 2, nums starts with [2, 2, ...]

Hint: A two-pointer write index that only advances when the element is not
equal to `val`.
"""


def remove_element(nums, val):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def remove_element(nums, val):
#     write = 0
#     for read in range(len(nums)):
#         if nums[read] != val:
#             nums[write] = nums[read]
#             write += 1
#     return write
