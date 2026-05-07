"""
Problem 67: Add Binary (Easy)

Given two binary strings `a` and `b`, return their sum as a binary string.

Example:
    Input:  a = "11",   b = "1"      -> "100"
    Input:  a = "1010", b = "1011"   -> "10101"

Hint: Walk both strings from the right, tracking a carry. Don't use int(.., 2)
on huge inputs -- it's a great fallback though.
"""


def add_binary(a, b):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def add_binary(a, b):
#     i, j = len(a) - 1, len(b) - 1
#     carry = 0
#     out = []
#     while i >= 0 or j >= 0 or carry:
#         total = carry
#         if i >= 0:
#             total += int(a[i]); i -= 1
#         if j >= 0:
#             total += int(b[j]); j -= 1
#         out.append(str(total % 2))
#         carry = total // 2
#     return ''.join(reversed(out))
