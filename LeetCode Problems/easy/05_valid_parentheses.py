"""
Problem 20: Valid Parentheses (Easy)

Given a string `s` containing just the characters '(', ')', '{', '}', '[', ']',
determine if the input string is valid. An input is valid if open brackets are
closed by the same type of brackets, and in the correct order.

Example:
    Input:  "()"        -> True
    Input:  "()[]{}"    -> True
    Input:  "(]"        -> False
    Input:  "([)]"      -> False

Hint: Use a stack. Push opens; on a close, the top must be its matching open.
"""


def is_valid(s):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def is_valid(s):
#     pairs = {')': '(', ']': '[', '}': '{'}
#     stack = []
#     for ch in s:
#         if ch in pairs:
#             if not stack or stack.pop() != pairs[ch]:
#                 return False
#         else:
#             stack.append(ch)
#     return not stack
