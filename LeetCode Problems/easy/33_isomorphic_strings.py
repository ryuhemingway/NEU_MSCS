"""
Problem 205: Isomorphic Strings (Easy)

Given two strings `s` and `t`, determine if they are isomorphic. Two strings
are isomorphic if characters in `s` can be replaced to get `t` -- with each
character mapping to exactly one other, and no two source chars mapping to
the same target.

Example:
    Input:  s = "egg",   t = "add"   -> True
    Input:  s = "foo",   t = "bar"   -> False
    Input:  s = "paper", t = "title" -> True

Hint: Two dicts (or check via index of first occurrence) -- s->t and t->s
must agree at every position.
"""


def is_isomorphic(s, t):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def is_isomorphic(s, t):
#     if len(s) != len(t):
#         return False
#     s_to_t, t_to_s = {}, {}
#     for a, b in zip(s, t):
#         if (a in s_to_t and s_to_t[a] != b) or \
#            (b in t_to_s and t_to_s[b] != a):
#             return False
#         s_to_t[a] = b
#         t_to_s[b] = a
#     return True
