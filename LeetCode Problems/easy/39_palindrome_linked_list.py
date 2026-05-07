"""
Problem 234: Palindrome Linked List (Easy)

Given the head of a singly linked list, return True if it is a palindrome.

Example:
    Input:  1 -> 2 -> 2 -> 1   -> True
    Input:  1 -> 2             -> False

Hint: Find the middle with slow/fast pointers, reverse the second half,
then compare halves. O(n) time, O(1) space.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def is_palindrome(head):
#     # find middle
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     # reverse second half
#     prev = None
#     while slow:
#         nxt = slow.next
#         slow.next = prev
#         prev = slow
#         slow = nxt
#     # compare
#     left, right = head, prev
#     while right:
#         if left.val != right.val:
#             return False
#         left = left.next
#         right = right.next
#     return True
