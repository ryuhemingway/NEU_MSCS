"""
Problem 242: Valid Anagram (Easy)

Given two strings `s` and `t`, return True if `t` is an anagram of `s` -- i.e.
they contain exactly the same characters in any order.

Example:
    Input:  s = "anagram", t = "nagaram"   -> True
    Input:  s = "rat",     t = "car"       -> False

Hint: Counting array of length 26 (or Counter): increment for s, decrement
for t; all zeros means anagram.
"""


def is_anagram(s, t):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def is_anagram(s, t):
#     if len(s) != len(t):
#         return False
#     count = [0] * 26
#     for cs, ct in zip(s, t):
#         count[ord(cs) - ord('a')] += 1
#         count[ord(ct) - ord('a')] -= 1
#     return all(c == 0 for c in count)
