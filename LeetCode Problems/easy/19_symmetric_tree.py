"""
Problem 101: Symmetric Tree (Easy)

Given the root of a binary tree, check whether it is a mirror of itself
(symmetric around its center).

Example:
    [1,2,2,3,4,4,3]      -> True
    [1,2,2,null,3,null,3] -> False

Hint: A tree is symmetric if its left and right subtrees mirror each other.
Compare in pairs: (left.left vs right.right) and (left.right vs right.left).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def is_symmetric(root):
#     def mirror(a, b):
#         if not a and not b:
#             return True
#         if not a or not b or a.val != b.val:
#             return False
#         return mirror(a.left, b.right) and mirror(a.right, b.left)
#     return mirror(root.left, root.right) if root else True
