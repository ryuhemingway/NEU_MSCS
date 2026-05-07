"""
Problem 75: Sort Colors (Medium)

Given an array `nums` with n objects colored red(0), white(1), or blue(2),
sort them in-place so the same colors are adjacent in the order 0, 1, 2.
Don't use a library sort.

Example:
    Input:  [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

Hint: Dutch National Flag algorithm. Three pointers low, mid, high. Walk mid
through the array; swap 0s to the front, 2s to the back; 1s stay put.
"""


def sort_colors(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def sort_colors(nums):
#     low, mid, high = 0, 0, len(nums) - 1
#     while mid <= high:
#         if nums[mid] == 0:
#             nums[low], nums[mid] = nums[mid], nums[low]
#             low += 1
#             mid += 1
#         elif nums[mid] == 1:
#             mid += 1
#         else:
#             nums[mid], nums[high] = nums[high], nums[mid]
#             high -= 1
