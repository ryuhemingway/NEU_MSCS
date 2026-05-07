"""
Problem 55: Jump Game (Medium)

You are given an integer array `nums`. You start at index 0. nums[i] is the
maximum jump length from i. Return True if you can reach the last index.

Example:
    Input:  [2,3,1,1,4]   -> True
    Input:  [3,2,1,0,4]   -> False

Hint: Greedy. Track the farthest index reachable so far. If at any point i
exceeds reach, return False. If reach >= last index, return True.
"""


def can_jump(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def can_jump(nums):
#     reach = 0
#     for i, jump in enumerate(nums):
#         if i > reach:
#             return False
#         reach = max(reach, i + jump)
#     return True
