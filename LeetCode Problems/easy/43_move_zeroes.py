"""
Problem 283: Move Zeroes (Easy)

Given an integer array `nums`, move all 0s to the end while maintaining the
relative order of the non-zero elements. Do it in-place, no copies.

Example:
    Input:  [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Hint: Two pointers -- write index for next non-zero slot. Walk through;
when nums[read] != 0, write it and advance write. After the pass, fill
nums[write:] with 0.
"""


def move_zeroes(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def move_zeroes(nums):
#     write = 0
#     for read in range(len(nums)):
#         if nums[read] != 0:
#             nums[write], nums[read] = nums[read], nums[write]
#             write += 1
