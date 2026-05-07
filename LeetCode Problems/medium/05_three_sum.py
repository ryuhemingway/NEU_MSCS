"""
Problem 15: 3Sum (Medium)

Given an integer array `nums`, return all unique triplets [a, b, c] such that
a + b + c == 0 and the triplets are not duplicates (in any order).

Example:
    Input:  [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

Hint: Sort, then for each i fix nums[i] and run two-pointer for the remaining
target -nums[i]. Skip duplicates carefully on i, left, and right.
"""


def three_sum(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def three_sum(nums):
#     nums.sort()
#     res = []
#     n = len(nums)
#     for i in range(n - 2):
#         if nums[i] > 0:
#             break
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         l, r = i + 1, n - 1
#         while l < r:
#             s = nums[i] + nums[l] + nums[r]
#             if s == 0:
#                 res.append([nums[i], nums[l], nums[r]])
#                 l += 1
#                 r -= 1
#                 while l < r and nums[l] == nums[l - 1]:
#                     l += 1
#                 while l < r and nums[r] == nums[r + 1]:
#                     r -= 1
#             elif s < 0:
#                 l += 1
#             else:
#                 r -= 1
#     return res
