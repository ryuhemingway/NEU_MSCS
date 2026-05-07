"""
Problem 39: Combination Sum (Medium)

Given an array of distinct positive integers `candidates` and a target, return
all unique combinations of candidates where the chosen numbers sum to target.
Each candidate may be used unlimited times. Combinations are unique if their
multisets differ.

Example:
    Input:  candidates = [2,3,6,7], target = 7
    Output: [[2,2,3], [7]]

Hint: Backtracking. Pass a `start` index so each recursion can pick the same
or later candidates -- prevents permutations of the same combo.
"""


def combination_sum(candidates, target):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def combination_sum(candidates, target):
#     res = []
#     path = []
#     def backtrack(start, remaining):
#         if remaining == 0:
#             res.append(path[:])
#             return
#         for i in range(start, len(candidates)):
#             if candidates[i] > remaining:
#                 continue
#             path.append(candidates[i])
#             backtrack(i, remaining - candidates[i])  # i, not i+1
#             path.pop()
#     backtrack(0, target)
#     return res
