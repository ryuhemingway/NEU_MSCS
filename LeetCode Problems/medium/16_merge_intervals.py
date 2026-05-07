"""
Problem 56: Merge Intervals (Medium)

Given an array of intervals where intervals[i] = [start_i, end_i], merge all
overlapping intervals and return the array of non-overlapping intervals that
cover all the input intervals.

Example:
    Input:  [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

Hint: Sort by start. Walk left to right -- if the current interval starts <=
the last merged interval's end, extend that merged end; otherwise append a
new merged interval.
"""


def merge(intervals):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def merge(intervals):
#     intervals.sort(key=lambda x: x[0])
#     merged = []
#     for start, end in intervals:
#         if merged and start <= merged[-1][1]:
#             merged[-1][1] = max(merged[-1][1], end)
#         else:
#             merged.append([start, end])
#     return merged
