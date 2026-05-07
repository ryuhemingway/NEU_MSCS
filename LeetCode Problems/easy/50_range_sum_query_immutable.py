"""
Problem 303: Range Sum Query - Immutable (Easy)

Given an integer array `nums`, implement NumArray with a method
sumRange(left, right) that returns the inclusive sum nums[left] + ... +
nums[right]. Many sumRange calls will be made on the same array.

Example:
    nums = [-2, 0, 3, -5, 2, -1]
    NumArray(nums).sumRange(0, 2)  -> 1   (-2 + 0 + 3)
    NumArray(nums).sumRange(2, 5)  -> -1
    NumArray(nums).sumRange(0, 5)  -> -3

Hint: Build a prefix-sum array in __init__ once. Each query is O(1):
prefix[right + 1] - prefix[left].
"""


class NumArray:
    def __init__(self, nums):
        # Your solution here
        pass

    def sumRange(self, left, right):
        pass


# ---------- Answer below (don't peek!) ----------
# class NumArray:
#     def __init__(self, nums):
#         self.prefix = [0] * (len(nums) + 1)
#         for i, n in enumerate(nums):
#             self.prefix[i + 1] = self.prefix[i] + n
#
#     def sumRange(self, left, right):
#         return self.prefix[right + 1] - self.prefix[left]
