"""
Problem 155: Min Stack (Easy)

Design a stack that supports push, pop, top, and retrieving the minimum
element -- all in O(1) time.

Methods:
    push(val), pop(), top(), get_min()

Example:
    s = MinStack()
    s.push(-2); s.push(0); s.push(-3)
    s.get_min()  # -3
    s.pop()
    s.top()      # 0
    s.get_min()  # -2

Hint: Keep a parallel "minimum so far" stack. When pushing, push min(val,
current_min). Pop both stacks together.
"""


class MinStack:
    def __init__(self):
        # Your solution here
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def get_min(self):
        pass


# ---------- Answer below (don't peek!) ----------
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.mins = []
#
#     def push(self, val):
#         self.stack.append(val)
#         self.mins.append(val if not self.mins else min(val, self.mins[-1]))
#
#     def pop(self):
#         self.stack.pop()
#         self.mins.pop()
#
#     def top(self):
#         return self.stack[-1]
#
#     def get_min(self):
#         return self.mins[-1]
