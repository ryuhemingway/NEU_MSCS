"""
Problem 122: Best Time to Buy and Sell Stock II (Medium)

You are given an integer array `prices` where prices[i] is the price on day
i. On each day you can buy and/or sell. You may hold at most one share at any
time. Return the maximum profit you can achieve.

Example:
    Input:  [7,1,5,3,6,4]   -> 7   (buy 1, sell 5; buy 3, sell 6)
    Input:  [1,2,3,4,5]     -> 4

Hint: Greedy. Capture every positive day-over-day gain; the sum of those is
the optimal profit (any longer-term profit decomposes into consecutive ones).
"""


def max_profit(prices):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def max_profit(prices):
#     profit = 0
#     for i in range(1, len(prices)):
#         if prices[i] > prices[i - 1]:
#             profit += prices[i] - prices[i - 1]
#     return profit
