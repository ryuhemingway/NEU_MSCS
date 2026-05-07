"""
Problem 9: Palindrome Number (Easy)

Given an integer `x`, return True if `x` is a palindrome, and False otherwise.
A palindrome reads the same forward and backward. Negative numbers are not
palindromes.

Example:
    Input:  x = 121     -> True
    Input:  x = -121    -> False
    Input:  x = 10      -> False

Hint: Try without converting to a string -- reverse half of the number and
compare it to the other half.
"""


def is_palindrome(x):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def is_palindrome(x):
#     if x < 0 or (x % 10 == 0 and x != 0):
#         return False
#     reversed_half = 0
#     while x > reversed_half:
#         reversed_half = reversed_half * 10 + x % 10
#         x //= 10
#     return x == reversed_half or x == reversed_half // 10
