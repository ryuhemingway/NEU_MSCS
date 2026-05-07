"""
Problem 207: Course Schedule (Medium)

There are `numCourses` numbered 0..numCourses-1. You are given prerequisites
where prerequisites[i] = [a, b] means to take course a you must first take b.
Return True if you can finish all courses (i.e., no cycle in dependencies).

Example:
    numCourses = 2, prerequisites = [[1, 0]]                -> True
    numCourses = 2, prerequisites = [[1, 0], [0, 1]]        -> False

Hint: Cycle detection on a directed graph. Easiest: Kahn's topological sort
-- count indegrees, repeatedly drain zero-indegree nodes; if you can't drain
all nodes, there's a cycle.
"""


def can_finish(num_courses, prerequisites):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def can_finish(num_courses, prerequisites):
#     from collections import defaultdict, deque
#     graph = defaultdict(list)
#     indeg = [0] * num_courses
#     for a, b in prerequisites:
#         graph[b].append(a)
#         indeg[a] += 1
#     q = deque(i for i in range(num_courses) if indeg[i] == 0)
#     taken = 0
#     while q:
#         node = q.popleft()
#         taken += 1
#         for nxt in graph[node]:
#             indeg[nxt] -= 1
#             if indeg[nxt] == 0:
#                 q.append(nxt)
#     return taken == num_courses
