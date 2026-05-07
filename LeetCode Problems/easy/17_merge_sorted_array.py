"""
Problem 88: Merge Sorted Array (Easy)

You are given two sorted integer arrays `nums1` (length m+n, last n slots are
zeros to be ignored) and `nums2` (length n). Merge `nums2` into `nums1` as one
sorted array, in-place.

Example:
    Input:  nums1 = [1, 2, 3, 0, 0, 0], m = 3
            nums2 = [2, 5, 6],          n = 3
    Output: nums1 = [1, 2, 2, 3, 5, 6]

Hint: Fill from the BACK of nums1 so you never overwrite an unread value.
Three pointers: end of nums1 valid region, end of nums2, write index.
"""


def merge(nums1, m, nums2, n):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def merge(nums1, m, nums2, n):
#     i, j, k = m - 1, n - 1, m + n - 1
#     while j >= 0:
#         if i >= 0 and nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k -= 1
