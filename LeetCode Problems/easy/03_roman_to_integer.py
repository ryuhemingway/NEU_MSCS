"""
Problem 13: Roman to Integer (Easy)

Roman numerals: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
Usually written largest to smallest, but six subtractive pairs exist:
IV=4, IX=9, XL=40, XC=90, CD=400, CM=900.
Given a roman numeral string `s`, convert it to an integer.

Example:
    Input:  "III"      -> 3
    Input:  "LVIII"    -> 58
    Input:  "MCMXCIV"  -> 1994

Hint: Walk left to right. If the current symbol is smaller than the next,
subtract it; otherwise add it.
"""


def roman_to_int(s):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def roman_to_int(s):
#     values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
#               'C': 100, 'D': 500, 'M': 1000}
#     total = 0
#     for i, ch in enumerate(s):
#         if i + 1 < len(s) and values[ch] < values[s[i + 1]]:
#             total -= values[ch]
#         else:
#             total += values[ch]
#     return total
