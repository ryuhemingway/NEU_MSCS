"""
Problem 225: Implement Stack using Queues (Easy)

Implement a LIFO stack using only standard queue operations (push to back,
pop from front, peek front, size, empty). Methods: push(x), pop(), top(),
empty().

Hint: Use a single queue. On push, enqueue then rotate the queue length-1
times so the new element is at the front. Now front == top of stack.
"""


from collections import deque


class MyStack:
    def __init__(self):
        # Your solution here
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def empty(self):
        pass


# ---------- Answer below (don't peek!) ----------
# class MyStack:
#     def __init__(self):
#         self.q = deque()
#
#     def push(self, x):
#         self.q.append(x)
#         for _ in range(len(self.q) - 1):
#             self.q.append(self.q.popleft())
#
#     def pop(self):
#         return self.q.popleft()
#
#     def top(self):
#         return self.q[0]
#
#     def empty(self):
#         return not self.q
