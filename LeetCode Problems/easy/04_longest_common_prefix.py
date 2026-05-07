"""
Problem 14: Longest Common Prefix (Easy)

Write a function to find the longest common prefix string amongst an array of
strings. If there is no common prefix, return "".

Example:
    Input:  ["flower", "flow", "flight"]   -> "fl"
    Input:  ["dog", "racecar", "car"]      -> ""

Hint: Compare characters column by column across all strings, or repeatedly
shrink a candidate prefix until every string starts with it.
"""


def longest_common_prefix(strs):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def longest_common_prefix(strs):
#     if not strs:
#         return ""
#     prefix = strs[0]
#     for s in strs[1:]:
#         while not s.startswith(prefix):
#             prefix = prefix[:-1]
#             if not prefix:
#                 return ""
#     return prefix
