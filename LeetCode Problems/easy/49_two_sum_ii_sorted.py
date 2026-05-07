"""
Problem 167: Two Sum II - Input Array Is Sorted (Easy)

Given a 1-indexed sorted array `numbers` and a target, return the two indices
[i, j] (1-indexed, i < j) of the two numbers that add up to target. There is
exactly one solution. Use only constant extra space.

Example:
    Input:  numbers = [2, 7, 11, 15], target = 9    -> [1, 2]
    Input:  numbers = [2, 3, 4],      target = 6    -> [1, 3]

Hint: Two pointers from both ends. If sum is too small, move left in; if too
big, move right in.
"""


def two_sum(numbers, target):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def two_sum(numbers, target):
#     i, j = 0, len(numbers) - 1
#     while i < j:
#         s = numbers[i] + numbers[j]
#         if s == target:
#             return [i + 1, j + 1]
#         elif s < target:
#             i += 1
#         else:
#             j -= 1
