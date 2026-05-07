"""
Problem 171: Excel Sheet Column Number (Easy)

Given a string `columnTitle` representing an Excel column title (e.g. "A",
"AB", "ZY"), return its corresponding column number. A=1, B=2, ..., Z=26,
AA=27, AB=28, ...

Example:
    Input:  "A"   -> 1
    Input:  "AB"  -> 28
    Input:  "ZY"  -> 701

Hint: Like base-26 with 'A' as 1 (no zero digit). Walk left to right,
result = result * 26 + (ord(c) - ord('A') + 1).
"""


def title_to_number(column_title):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def title_to_number(column_title):
#     result = 0
#     for ch in column_title:
#         result = result * 26 + (ord(ch) - ord('A') + 1)
#     return result
