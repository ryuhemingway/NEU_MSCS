"""
Problem 215: Kth Largest Element in an Array (Medium)

Given an integer array `nums` and an integer `k`, return the k-th largest
element in the array. Note: it is the k-th largest in sorted order, not the
k-th distinct.

Example:
    Input:  nums = [3,2,1,5,6,4], k = 2     -> 5
    Input:  nums = [3,2,3,1,2,4,5,5,6], k = 4  -> 4

Hint: Easiest: maintain a min-heap of size k. For each element, push and pop
if size exceeds k. The root is the k-th largest at the end. O(n log k).
Quickselect gets O(n) average but is trickier.
"""


def find_kth_largest(nums, k):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def find_kth_largest(nums, k):
#     import heapq
#     heap = []
#     for n in nums:
#         heapq.heappush(heap, n)
#         if len(heap) > k:
#             heapq.heappop(heap)
#     return heap[0]
