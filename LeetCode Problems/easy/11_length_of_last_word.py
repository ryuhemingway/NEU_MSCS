"""
Problem 58: Length of Last Word (Easy)

Given a string `s` consisting of words and spaces, return the length of the
last word. A word is a maximal substring of non-space characters.

Example:
    Input:  "Hello World"             -> 5
    Input:  "   fly me   to   the moon"  -> 4

Hint: Walk from the right, skip trailing spaces, then count until you hit a
space or run out of string.
"""


def length_of_last_word(s):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def length_of_last_word(s):
#     i = len(s) - 1
#     while i >= 0 and s[i] == ' ':
#         i -= 1
#     length = 0
#     while i >= 0 and s[i] != ' ':
#         length += 1
#         i -= 1
#     return length
