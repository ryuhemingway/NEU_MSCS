"""
Problem 383: Ransom Note (Easy)

Given two strings `ransomNote` and `magazine`, return True if `ransomNote` can
be constructed using letters from `magazine`. Each magazine letter may be used
at most once.

Example:
    Input:  ransomNote = "a",   magazine = "b"    -> False
    Input:  ransomNote = "aa",  magazine = "ab"   -> False
    Input:  ransomNote = "aa",  magazine = "aab"  -> True

Hint: Counter(magazine) must be >= Counter(ransomNote) for every key.
"""


def can_construct(ransom_note, magazine):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def can_construct(ransom_note, magazine):
#     from collections import Counter
#     mag = Counter(magazine)
#     for ch, need in Counter(ransom_note).items():
#         if mag[ch] < need:
#             return False
#     return True
