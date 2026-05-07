"""
Problem 49: Group Anagrams (Medium)

Given an array of strings `strs`, group the anagrams together. Return the
groups in any order.

Example:
    Input:  ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Hint: Map a canonical key for each string (sorted chars, OR a length-26 count
tuple) to the list of words that share it.
"""


def group_anagrams(strs):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def group_anagrams(strs):
#     from collections import defaultdict
#     groups = defaultdict(list)
#     for s in strs:
#         key = tuple(sorted(s))         # or count tuple of len 26
#         groups[key].append(s)
#     return list(groups.values())
