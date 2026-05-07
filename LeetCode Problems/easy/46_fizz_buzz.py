"""
Problem 412: Fizz Buzz (Easy)

Given an integer `n`, return a string array `answer` (1-indexed) where:
    answer[i] == "FizzBuzz" if i is divisible by 3 and 5
    answer[i] == "Fizz"     if i is divisible by 3
    answer[i] == "Buzz"     if i is divisible by 5
    answer[i] == str(i)     otherwise

Example:
    Input:  n = 5
    Output: ["1", "2", "Fizz", "4", "Buzz"]

Hint: Simple loop. Bonus: try checking divisibility by 15 first to avoid two
modulus checks.
"""


def fizz_buzz(n):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def fizz_buzz(n):
#     out = []
#     for i in range(1, n + 1):
#         if i % 15 == 0:
#             out.append("FizzBuzz")
#         elif i % 3 == 0:
#             out.append("Fizz")
#         elif i % 5 == 0:
#             out.append("Buzz")
#         else:
#             out.append(str(i))
#     return out
