"""
Problem 198: House Robber (Medium)

You are a robber planning to rob houses along a street. Each house has some
amount of money; you can't rob two adjacent houses (they alert the police).
Given an array `nums`, return the maximum amount you can rob.

Example:
    Input:  [1,2,3,1]       -> 4   (rob 1 and 3)
    Input:  [2,7,9,3,1]     -> 12  (rob 2, 9, 1)

Hint: DP recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i]). Reduce to two
rolling variables.
"""


def rob(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def rob(nums):
#     prev2, prev1 = 0, 0
#     for n in nums:
#         prev2, prev1 = prev1, max(prev1, prev2 + n)
#     return prev1
