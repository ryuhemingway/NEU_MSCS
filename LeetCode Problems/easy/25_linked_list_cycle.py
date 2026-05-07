"""
Problem 141: Linked List Cycle (Easy)

Given the head of a linked list, determine whether the list has a cycle. A
cycle exists if some node can be reached again by continuously following the
next pointer.

Example:
    3 -> 2 -> 0 -> -4 -> (back to 2)   -> True
    1 -> 2                              -> False

Hint: Floyd's tortoise & hare. A slow pointer (1 step) and fast pointer (2
steps) will meet inside any cycle and never meet without one.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def has_cycle(head):
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow is fast:
#             return True
#     return False
