"""
Problem 5: Longest Palindromic Substring (Medium)

Given a string `s`, return the longest palindromic substring in `s`.

Example:
    Input:  "babad"   -> "bab" (or "aba")
    Input:  "cbbd"    -> "bb"

Hint: For each index, "expand around center" considering both odd-length
(single char center) and even-length (two-char center) palindromes. O(n^2)
time, O(1) space.
"""


def longest_palindrome(s):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def longest_palindrome(s):
#     def expand(l, r):
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             l -= 1
#             r += 1
#         return l + 1, r - 1
#
#     start, end = 0, 0
#     for i in range(len(s)):
#         l1, r1 = expand(i, i)
#         l2, r2 = expand(i, i + 1)
#         if r1 - l1 > end - start:
#             start, end = l1, r1
#         if r2 - l2 > end - start:
#             start, end = l2, r2
#     return s[start:end + 1]
