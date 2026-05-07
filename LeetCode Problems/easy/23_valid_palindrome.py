"""
Problem 125: Valid Palindrome (Easy)

A phrase is a palindrome if, after converting all uppercase letters to
lowercase and removing all non-alphanumeric characters, it reads the same
forward and backward. Given a string `s`, return True if it's a palindrome.

Example:
    Input:  "A man, a plan, a canal: Panama"   -> True
    Input:  "race a car"                       -> False

Hint: Two pointers from both ends; skip non-alphanumeric chars; compare
case-insensitively.
"""


def is_palindrome(s):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def is_palindrome(s):
#     i, j = 0, len(s) - 1
#     while i < j:
#         while i < j and not s[i].isalnum():
#             i += 1
#         while i < j and not s[j].isalnum():
#             j -= 1
#         if s[i].lower() != s[j].lower():
#             return False
#         i += 1
#         j -= 1
#     return True
