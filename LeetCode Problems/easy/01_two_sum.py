"""
Problem 1: Two Sum (Easy)

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers such that they add up to `target`. You may assume each input
has exactly one solution, and you may not use the same element twice.

Example:
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]   (because nums[0] + nums[1] == 9)

Hint: A nested loop is O(n^2). Can you do it in one pass with a hash map
storing each value's index as you go?
"""


def two_sum(nums, target):
    # Your solution here
    pass



























# ---------- Answer below (don't peek!) ----------
# def two_sum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i
