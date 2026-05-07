"""
Problem 78: Subsets (Medium)

Given an integer array `nums` of unique elements, return all possible subsets
(the power set). The solution set must not contain duplicate subsets.

Example:
    Input:  [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Hint: Two clean approaches: (a) iterative -- start with [[]] and for each
num, append num to copies of every existing subset; (b) backtracking with a
start index.
"""


def subsets(nums):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def subsets(nums):
#     res = [[]]
#     for n in nums:
#         res += [sub + [n] for sub in res]
#     return res
