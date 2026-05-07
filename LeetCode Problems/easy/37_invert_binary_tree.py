"""
Problem 226: Invert Binary Tree (Easy)

Given the root of a binary tree, invert it (swap every node's left and right
subtree) and return the root.

Example:
    Input:    4
            /   \\
           2     7
          / \\   / \\
         1   3 6   9
    Output:   4
            /   \\
           7     2
          / \\   / \\
         9   6 3   1

Hint: Recurse: swap left and right, then invert each subtree. The classic
one-liner.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def invert_tree(root):
#     if not root:
#         return None
#     root.left, root.right = invert_tree(root.right), invert_tree(root.left)
#     return root
