"""
Problem 160: Intersection of Two Linked Lists (Easy)

Given the heads of two singly linked lists `headA` and `headB`, return the
node at which they intersect, or None if they do not intersect.

Example:
    A: 4 -> 1 \
                8 -> 4 -> 5
    B: 5 -> 6 -> 1 /
    -> intersection node has val 8

Hint: Two pointers. When one reaches the end, redirect to the other list's
head. After at most m+n steps they meet at the intersection (or both at None).
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_intersection_node(headA, headB):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def get_intersection_node(headA, headB):
#     if not headA or not headB:
#         return None
#     a, b = headA, headB
#     while a is not b:
#         a = a.next if a else headB
#         b = b.next if b else headA
#     return a
