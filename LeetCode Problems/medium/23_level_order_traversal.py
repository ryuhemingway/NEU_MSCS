"""
Problem 102: Binary Tree Level Order Traversal (Medium)

Given the root of a binary tree, return the level order traversal of its node
values (left to right, level by level).

Example:
    Input:  [3,9,20,null,null,15,7]
    Output: [[3], [9,20], [15,7]]

Hint: BFS with a queue. At each iteration, capture the current level size
upfront and process exactly that many nodes before moving to the next level.
"""


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def level_order(root):
#     if not root:
#         return []
#     res = []
#     q = deque([root])
#     while q:
#         level = []
#         for _ in range(len(q)):
#             node = q.popleft()
#             level.append(node.val)
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         res.append(level)
#     return res
