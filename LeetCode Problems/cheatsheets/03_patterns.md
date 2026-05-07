# Algorithm Pattern Templates

Each template is a copy-pasteable starting point — adapt to the specific problem.

## 1. Two Pointers (sorted array)
**When:** sorted array, find pair/triplet with property; in-place dedup; reverse.
```python
def two_sum_sorted(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            return [i, j]
        elif s < target:
            i += 1
        else:
            j -= 1
```

## 2. Fast & Slow Pointers (cycle / midpoint)
**When:** linked list cycle detection, find middle, palindrome on linked list.
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow is fast:
        return True   # cycle
# At end of loop, slow is at middle
```

## 3. Sliding Window (variable size)
**When:** longest/shortest substring with property, max sum subarray of size k.
```python
def longest_unique_substring(s):
    seen = {}                    # char -> last index
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

Fixed-size window:
```python
def max_sum_window(arr, k):
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        best = max(best, window)
    return best
```

## 4. Binary Search
**When:** sorted input, OR monotonic predicate `f(x)` you can binary search on.
```python
def bsearch(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1   # or `lo` for insertion point
```

Binary search on the answer:
```python
def min_capacity(weights, days):
    def feasible(cap):
        # can we ship in <= days at this capacity?
        ...
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## 5. BFS (queue, shortest path on unweighted graph / level order)
```python
from collections import deque
def bfs(start, neighbors):
    visited = {start}
    queue = deque([(start, 0)])    # (node, distance)
    while queue:
        node, dist = queue.popleft()
        if is_goal(node):
            return dist
        for nb in neighbors(node):
            if nb not in visited:
                visited.add(nb)
                queue.append((nb, dist + 1))
    return -1
```

## 6. DFS (recursive, exhaustive exploration)
```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    # process(node)
    for nb in neighbors(node):
        dfs(nb, visited)
```

Iterative (when depth might overflow):
```python
def dfs_iter(start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for nb in neighbors(node):
            if nb not in visited:
                stack.append(nb)
```

## 7. Backtracking (build / undo)
**When:** all subsets, all permutations, N-queens, sudoku, word search.
```python
def subsets(nums):
    result = []
    path = []
    def backtrack(i):
        if i == len(nums):
            result.append(path[:])     # copy!
            return
        # exclude nums[i]
        backtrack(i + 1)
        # include nums[i]
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()                     # undo
    backtrack(0)
    return result
```

## 8. Dynamic Programming
**Steps:**
1. Define state — what does dp[i] (or dp[i][j]) mean?
2. Recurrence — dp[i] in terms of smaller states.
3. Base case.
4. Order of computation.
5. Optimize space if rows only depend on the last few.

1D DP (climbing stairs / house robber style):
```python
def rob(nums):
    prev2, prev1 = 0, 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1
```

2D DP (grid):
```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
```

Memoized recursion (top-down):
```python
from functools import lru_cache
@lru_cache(maxsize=None)
def solve(i, j):
    if base_case: return ...
    return min(solve(i-1, j), solve(i, j-1)) + cost(i, j)
```

## 9. Topological Sort (Kahn's)
**When:** scheduling / dependency order. Detects cycles.
```python
from collections import deque, defaultdict
def topo(num_nodes, edges):       # edges = [(u, v)] meaning u -> v
    indeg = [0] * num_nodes
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(num_nodes) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == num_nodes else []   # [] if cycle
```

## 10. Union-Find / DSU
**When:** connected components, Kruskal's MST, "are these two in the same group?".
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path compression
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True
```

## 11. Heap (Top-K, scheduling)
```python
import heapq
def top_k_largest(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap                # k largest, unsorted
```

## 12. Trie
```python
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word):
        node = self
        for ch in word:
            node = node.children.setdefault(ch, Trie())
        node.end = True

    def search(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end
```

## 13. Bit Tricks
```python
x & (x - 1)        # clears the lowest set bit (used in is-power-of-two)
x & -x             # isolates the lowest set bit
bin(x).count('1')  # popcount
x ^ y              # XOR — toggle, or "find odd one out"
x | (1 << k)       # set bit k
x & ~(1 << k)      # clear bit k
(x >> k) & 1       # read bit k
# Iterate subsets of mask: sub = mask; while sub: ...; sub = (sub - 1) & mask
```

## 14. Prefix Sum / Difference Array
```python
prefix = [0] * (len(arr) + 1)
for i, v in enumerate(arr):
    prefix[i + 1] = prefix[i] + v
# range sum [l..r] inclusive = prefix[r + 1] - prefix[l]
```

Difference array (range update, point query):
```python
diff = [0] * (n + 1)
for l, r, x in updates:
    diff[l] += x
    diff[r + 1] -= x
# Apply: arr[i] = prefix sum of diff
```

## 15. Monotonic Stack (next greater / smaller)
```python
def next_greater(nums):
    res = [-1] * len(nums)
    stack = []   # indices, values strictly decreasing
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            res[stack.pop()] = n
        stack.append(i)
    return res
```

## How to recognize patterns from the prompt

| Words in problem            | Likely pattern                  |
|-----------------------------|---------------------------------|
| sorted array                | binary search OR two pointers   |
| "all", "every", "subset"    | backtracking / bitmask          |
| "shortest path" (unweighted)| BFS                             |
| "minimum cost / weighted"   | Dijkstra / DP                   |
| "longest / max ... such that"| sliding window / DP            |
| top-k, k smallest/largest   | heap                            |
| "are they connected"        | Union-Find or DFS/BFS           |
| dependencies, prereqs       | topological sort                |
| substring / subarray sums   | prefix sum / sliding window     |
| "next greater/smaller"      | monotonic stack                 |
| palindrome                  | two pointers OR DP              |
| count distinct in window    | sliding window + Counter        |
| 2 of each, 1 unique         | XOR                             |
