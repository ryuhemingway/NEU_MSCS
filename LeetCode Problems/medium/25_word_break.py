"""
Problem 139: Word Break (Medium)

Given a string `s` and a list of strings `wordDict`, return True if `s` can
be segmented into a space-separated sequence of one or more dictionary words.
Words may be reused.

Example:
    Input:  s = "leetcode", wordDict = ["leet","code"]   -> True
    Input:  s = "applepenapple", wordDict = ["apple","pen"] -> True
    Input:  s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] -> False

Hint: DP. dp[i] = "can s[:i] be segmented". dp[0] = True. For each i, set
dp[i] = True if any j < i has dp[j] and s[j:i] in wordDict.
"""


def word_break(s, word_dict):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def word_break(s, word_dict):
#     words = set(word_dict)
#     n = len(s)
#     dp = [False] * (n + 1)
#     dp[0] = True
#     for i in range(1, n + 1):
#         for j in range(i):
#             if dp[j] and s[j:i] in words:
#                 dp[i] = True
#                 break
#     return dp[n]
