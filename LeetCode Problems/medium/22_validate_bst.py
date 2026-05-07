"""
Problem 98: Validate Binary Search Tree (Medium)

Given the root of a binary tree, determine if it is a valid BST. A valid BST:
left subtree contains only values < node, right subtree contains only values
> node, and both subtrees must themselves be valid BSTs.

Example:
        2
       / \\
      1   3       -> True

        5
       / \\
      1   4
         / \\
        3   6     -> False (3 lives in 5's right subtree but is < 5)

Hint: Pass a (low, high) range down. Each node's value must satisfy
low < val < high; left child gets high=val, right child gets low=val.
Inorder traversal also works -- it must be strictly increasing.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def is_valid_bst(root):
#     def validate(node, low, high):
#         if not node:
#             return True
#         if not (low < node.val < high):
#             return False
#         return (validate(node.left, low, node.val)
#                 and validate(node.right, node.val, high))
#     return validate(root, float('-inf'), float('inf'))
