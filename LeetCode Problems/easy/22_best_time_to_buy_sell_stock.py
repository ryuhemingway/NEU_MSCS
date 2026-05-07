"""
Problem 121: Best Time to Buy and Sell Stock (Easy)

Given an array `prices` where prices[i] is the price of a stock on day i, find
the maximum profit you can achieve by buying once and selling later. If no
profit is possible, return 0.

Example:
    Input:  [7, 1, 5, 3, 6, 4]   -> 5   (buy at 1, sell at 6)
    Input:  [7, 6, 4, 3, 1]      -> 0

Hint: Single pass -- track the minimum price seen so far and the best profit
achievable selling at the current price.
"""


def max_profit(prices):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def max_profit(prices):
#     min_price = float('inf')
#     best = 0
#     for p in prices:
#         if p < min_price:
#             min_price = p
#         elif p - min_price > best:
#             best = p - min_price
#     return best
