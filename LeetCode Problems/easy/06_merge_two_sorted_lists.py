"""
Problem 21: Merge Two Sorted Lists (Easy)

You are given the heads of two sorted linked lists `list1` and `list2`. Merge
the two lists into a single sorted list by splicing together the nodes. Return
the head of the merged list.

Example:
    list1 = 1 -> 2 -> 4
    list2 = 1 -> 3 -> 4
    output = 1 -> 1 -> 2 -> 3 -> 4 -> 4

Hint: Use a dummy head and a tail pointer. At each step, attach the smaller
node and advance.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def merge_two_lists(list1, list2):
#     dummy = ListNode()
#     tail = dummy
#     while list1 and list2:
#         if list1.val <= list2.val:
#             tail.next = list1
#             list1 = list1.next
#         else:
#             tail.next = list2
#             list2 = list2.next
#         tail = tail.next
#     tail.next = list1 or list2
#     return dummy.next
