"""
Problem 3: Longest Substring Without Repeating Characters (Medium)

Given a string `s`, find the length of the longest substring without repeating
characters.

Example:
    Input:  "abcabcbb"  -> 3   ("abc")
    Input:  "bbbbb"     -> 1   ("b")
    Input:  "pwwkew"    -> 3   ("wke")

Hint: Sliding window with a hash map of char -> latest index. When you see a
repeat inside the window, jump `left` to one past the previous occurrence.
"""


def length_of_longest_substring(s):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def length_of_longest_substring(s):
#     last_seen = {}
#     left = 0
#     best = 0
#     for right, ch in enumerate(s):
#         if ch in last_seen and last_seen[ch] >= left:
#             left = last_seen[ch] + 1
#         last_seen[ch] = right
#         best = max(best, right - left + 1)
#     return best
