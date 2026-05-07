"""
Problem 19: Remove Nth Node From End of List (Medium)

Given the head of a linked list, remove the n-th node from the end and return
the head. Try to do it in one pass.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5, n = 2
    Output: 1 -> 2 -> 3 -> 5

Hint: Use a dummy head. Two pointers — advance fast n+1 steps first, then move
both until fast hits None. Slow now sits at the node BEFORE the one to remove.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def remove_nth_from_end(head, n):
#     dummy = ListNode(0, head)
#     fast = slow = dummy
#     for _ in range(n + 1):
#         fast = fast.next
#     while fast:
#         fast = fast.next
#         slow = slow.next
#     slow.next = slow.next.next
#     return dummy.next
