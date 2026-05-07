"""
Problem 206: Reverse Linked List (Easy)

Given the head of a singly linked list, reverse the list, and return the new
head.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1

Hint: Iterative -- prev=None, curr=head. Each step: save next, point curr.next
back to prev, advance prev=curr, curr=saved next.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def reverse_list(head):
#     prev = None
#     curr = head
#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt
#     return prev
