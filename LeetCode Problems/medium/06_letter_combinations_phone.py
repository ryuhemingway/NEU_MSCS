"""
Problem 17: Letter Combinations of a Phone Number (Medium)

Given a string `digits` containing digits 2-9, return all possible letter
combinations the number could represent (phone keypad mapping).

    2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz

Example:
    Input:  "23"   -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    Input:  ""     -> []

Hint: Backtracking. Build a path char-by-char; recurse one digit deeper; pop
on return.
"""


def letter_combinations(digits):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def letter_combinations(digits):
#     if not digits:
#         return []
#     mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl',
#                '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
#     res = []
#     path = []
#     def backtrack(i):
#         if i == len(digits):
#             res.append(''.join(path))
#             return
#         for ch in mapping[digits[i]]:
#             path.append(ch)
#             backtrack(i + 1)
#             path.pop()
#     backtrack(0)
#     return res
