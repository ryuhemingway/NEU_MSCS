"""
Problem 232: Implement Queue using Stacks (Easy)

Implement a FIFO queue using only stack operations (push, pop, peek, empty).
Methods: push(x), pop(), peek(), empty(). Each method should be amortized
O(1).

Hint: Two stacks: `in_stack` for pushes, `out_stack` for pops/peeks. When
out_stack is empty and you need to pop/peek, pour all of in_stack into
out_stack -- this reverses order.
"""


class MyQueue:
    def __init__(self):
        # Your solution here
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def empty(self):
        pass


# ---------- Answer below (don't peek!) ----------
# class MyQueue:
#     def __init__(self):
#         self.in_stack = []
#         self.out_stack = []
#
#     def push(self, x):
#         self.in_stack.append(x)
#
#     def _shift(self):
#         if not self.out_stack:
#             while self.in_stack:
#                 self.out_stack.append(self.in_stack.pop())
#
#     def pop(self):
#         self._shift()
#         return self.out_stack.pop()
#
#     def peek(self):
#         self._shift()
#         return self.out_stack[-1]
#
#     def empty(self):
#         return not self.in_stack and not self.out_stack
