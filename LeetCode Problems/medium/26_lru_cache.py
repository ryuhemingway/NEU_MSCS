"""
Problem 146: LRU Cache (Medium)

Design a Least Recently Used (LRU) cache with capacity `capacity`. Implement:
    get(key)        -> value if present, else -1
    put(key, value) -> add/update; evict the LRU item if over capacity
Both must run in O(1) average time.

Hint: Hash map + doubly-linked list. The list keeps order: most recent at one
end, least recent at the other. The hash map gives O(1) node lookup. In
Python you can cheat with collections.OrderedDict (move_to_end / popitem).
"""


from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        # Your solution here
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass


# ---------- Answer below (don't peek!) ----------
# class LRUCache:
#     def __init__(self, capacity):
#         self.cap = capacity
#         self.cache = OrderedDict()
#
#     def get(self, key):
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]
#
#     def put(self, key, value):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value
#         if len(self.cache) > self.cap:
#             self.cache.popitem(last=False)
