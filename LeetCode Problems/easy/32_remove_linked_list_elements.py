"""
Problem 203: Remove Linked List Elements (Easy)

Given the head of a linked list and an integer `val`, remove all nodes whose
value equals `val` and return the new head.

Example:
    Input:  head = 1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5

Hint: Use a dummy node before head to gracefully handle deletion of the
original head. Walk with a prev pointer.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head, val):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def remove_elements(head, val):
#     dummy = ListNode(0, head)
#     curr = dummy
#     while curr.next:
#         if curr.next.val == val:
#             curr.next = curr.next.next
#         else:
#             curr = curr.next
#     return dummy.next
