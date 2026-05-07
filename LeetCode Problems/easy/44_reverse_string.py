"""
Problem 344: Reverse String (Easy)

Write a function that reverses a string. The input is given as an array of
characters `s`. Modify in-place with O(1) extra memory.

Example:
    Input:  ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Hint: Two pointers, swap and converge.
"""


def reverse_string(s):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def reverse_string(s):
#     i, j = 0, len(s) - 1
#     while i < j:
#         s[i], s[j] = s[j], s[i]
#         i += 1
#         j -= 1
