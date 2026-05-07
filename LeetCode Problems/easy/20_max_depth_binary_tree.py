"""
Problem 104: Maximum Depth of Binary Tree (Easy)

Given the root of a binary tree, return its maximum depth (the number of nodes
along the longest path from the root down to the farthest leaf).

Example:
    [3,9,20,null,null,15,7]  -> 3

Hint: max_depth(node) = 1 + max(max_depth(left), max_depth(right)). Base case
is a null node returning 0.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def max_depth(root):
#     if not root:
#         return 0
#     return 1 + max(max_depth(root.left), max_depth(root.right))
