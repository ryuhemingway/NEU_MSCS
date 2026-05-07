"""
Problem 2: Add Two Numbers (Medium)

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in REVERSE order, one digit per node. Add the
two numbers and return the sum as a linked list, also in reverse order.

Example:
    l1 = 2 -> 4 -> 3   (represents 342)
    l2 = 5 -> 6 -> 4   (represents 465)
    output = 7 -> 0 -> 8   (807)

Hint: Walk both lists in parallel, tracking a carry. Don't forget the final
carry node if it's non-zero. A dummy head simplifies the build.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def add_two_numbers(l1, l2):
#     dummy = ListNode()
#     tail = dummy
#     carry = 0
#     while l1 or l2 or carry:
#         total = carry
#         if l1:
#             total += l1.val; l1 = l1.next
#         if l2:
#             total += l2.val; l2 = l2.next
#         carry, digit = divmod(total, 10)
#         tail.next = ListNode(digit)
#         tail = tail.next
#     return dummy.next
