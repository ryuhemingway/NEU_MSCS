"""
Problem 387: First Unique Character in a String (Easy)

Given a string `s`, return the index of the first non-repeating character. If
none exists, return -1.

Example:
    Input:  "leetcode"      -> 0
    Input:  "loveleetcode"  -> 2
    Input:  "aabb"          -> -1

Hint: First pass: count each char. Second pass: return the first index whose
count is 1.
"""


def first_uniq_char(s):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def first_uniq_char(s):
#     from collections import Counter
#     counts = Counter(s)
#     for i, ch in enumerate(s):
#         if counts[ch] == 1:
#             return i
#     return -1
