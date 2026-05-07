"""
Problem 136: Single Number (Easy)

Given a non-empty array of integers `nums`, every element appears twice except
for one. Find that single one. Must be O(n) time and O(1) extra space.

Example:
    Input:  [2, 2, 1]      -> 1
    Input:  [4, 1, 2, 1, 2] -> 4

Hint: XOR has two key properties: x ^ x == 0, and x ^ 0 == x. XOR everything
together and only the unique value survives.
"""


def single_number(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def single_number(nums):
#     result = 0
#     for n in nums:
#         result ^= n
#     return result
