"""
Problem 83: Remove Duplicates from Sorted List (Easy)

Given the head of a sorted linked list, delete all duplicates so that each
element appears only once. Return the modified list head.

Example:
    Input:  1 -> 1 -> 2          -> 1 -> 2
    Input:  1 -> 1 -> 2 -> 3 -> 3 -> 1 -> 2 -> 3

Hint: A single pass: if curr.val == curr.next.val, splice out curr.next;
otherwise advance.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def delete_duplicates(head):
#     curr = head
#     while curr and curr.next:
#         if curr.val == curr.next.val:
#             curr.next = curr.next.next
#         else:
#             curr = curr.next
#     return head
