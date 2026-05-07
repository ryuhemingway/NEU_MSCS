"""
Problem 22: Generate Parentheses (Medium)

Given n pairs of parentheses, generate all combinations of well-formed
parentheses.

Example:
    Input:  n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Hint: Backtracking with two counters: open_used and close_used. You can place
'(' if open_used < n; you can place ')' only if close_used < open_used.
"""


def generate_parenthesis(n):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def generate_parenthesis(n):
#     res = []
#     def backtrack(curr, opens, closes):
#         if len(curr) == 2 * n:
#             res.append(curr)
#             return
#         if opens < n:
#             backtrack(curr + '(', opens + 1, closes)
#         if closes < opens:
#             backtrack(curr + ')', opens, closes + 1)
#     backtrack('', 0, 0)
#     return res
