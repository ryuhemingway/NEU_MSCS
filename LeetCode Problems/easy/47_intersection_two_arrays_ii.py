"""
Problem 350: Intersection of Two Arrays II (Easy)

Given two integer arrays `nums1` and `nums2`, return an array of their
intersection. Each element in the result must appear as many times as it
shows in both arrays. The result can be in any order.

Example:
    Input:  nums1 = [1,2,2,1], nums2 = [2,2]      -> [2,2]
    Input:  nums1 = [4,9,5],   nums2 = [9,4,9,8,4] -> [4,9]

Hint: Use Counter on the smaller array; iterate the larger and pull until
the count for that value runs out.
"""


def intersect(nums1, nums2):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def intersect(nums1, nums2):
#     from collections import Counter
#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1
#     counts = Counter(nums1)
#     out = []
#     for n in nums2:
#         if counts[n] > 0:
#             out.append(n)
#             counts[n] -= 1
#     return out
