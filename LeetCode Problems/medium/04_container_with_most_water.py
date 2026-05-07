"""
Problem 11: Container With Most Water (Medium)

Given an integer array `height` where height[i] is the height of a vertical
line at x = i, find two lines that together with the x-axis form a container
holding the most water. Return that maximum area.

Example:
    Input:  [1,8,6,2,5,4,8,3,7]   -> 49

Hint: Two pointers from both ends. Always move the SHORTER side inward —
moving the taller side cannot increase area (width shrinks, height capped).
"""


def max_area(height):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def max_area(height):
#     i, j = 0, len(height) - 1
#     best = 0
#     while i < j:
#         h = min(height[i], height[j])
#         best = max(best, h * (j - i))
#         if height[i] < height[j]:
#             i += 1
#         else:
#             j -= 1
#     return best
