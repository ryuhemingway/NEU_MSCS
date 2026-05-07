"""
Problem 100: Same Tree (Easy)

Given the roots of two binary trees `p` and `q`, return True if they are the
same tree (identical structure and values), else False.

Example:
    p = [1,2,3], q = [1,2,3]  -> True
    p = [1,2],   q = [1,null,2] -> False

Hint: Recurse: both null -> True; one null -> False; values differ -> False;
otherwise both subtrees must match.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def is_same_tree(p, q):
#     if not p and not q:
#         return True
#     if not p or not q or p.val != q.val:
#         return False
#     return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
