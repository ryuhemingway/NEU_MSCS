"""
Problem 28: Find the Index of the First Occurrence in a String (Easy)

Given two strings `haystack` and `needle`, return the index of the first
occurrence of `needle` in `haystack`, or -1 if `needle` is not part of
`haystack`.

Example:
    Input:  haystack = "sadbutsad", needle = "sad"   -> 0
    Input:  haystack = "leetcode",  needle = "leeto" -> -1

Hint: Slide a window of length len(needle) across haystack and compare. (Yes,
str.find exists -- try doing it manually for practice.)
"""


def str_str(haystack, needle):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def str_str(haystack, needle):
#     n, m = len(haystack), len(needle)
#     if m == 0:
#         return 0
#     for i in range(n - m + 1):
#         if haystack[i:i + m] == needle:
#             return i
#     return -1
