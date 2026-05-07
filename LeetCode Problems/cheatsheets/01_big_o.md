# Big-O Cheat Sheet

## Growth rates (slow → fast)
`O(1) < O(log n) < O(sqrt n) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)`

Rule of thumb at n = 10^6:
- O(log n) ≈ 20 ops
- O(n) ≈ 10^6 ops (fine)
- O(n log n) ≈ 2×10^7 (fine)
- O(n^2) ≈ 10^12 (too slow)

## Python data structures

| Operation             | list   | tuple  | dict   | set    | deque  |
|-----------------------|--------|--------|--------|--------|--------|
| Index access `a[i]`   | O(1)   | O(1)   | O(1)   | —      | O(n)   |
| Append / push back    | O(1)*  | —      | —      | —      | O(1)   |
| Pop back              | O(1)   | —      | —      | —      | O(1)   |
| Insert / pop front    | O(n)   | —      | —      | —      | O(1)   |
| Membership `x in a`   | O(n)   | O(n)   | O(1)   | O(1)   | O(n)   |
| `a.remove(x)`         | O(n)   | —      | —      | O(1)   | O(n)   |
| `min/max`             | O(n)   | O(n)   | O(n)   | O(n)   | O(n)   |
| Sort                  | O(n log n) | — | — | — | — |

`*` amortized

## Sorting and searching

| Algorithm      | Best       | Average    | Worst      | Space  | Stable |
|----------------|------------|------------|------------|--------|--------|
| Quicksort      | O(n log n) | O(n log n) | O(n^2)     | O(log n) | No   |
| Mergesort      | O(n log n) | O(n log n) | O(n log n) | O(n)   | Yes    |
| Heapsort       | O(n log n) | O(n log n) | O(n log n) | O(1)   | No     |
| Timsort (Python) | O(n)     | O(n log n) | O(n log n) | O(n)   | Yes    |
| Insertion      | O(n)       | O(n^2)     | O(n^2)     | O(1)   | Yes    |
| Bubble         | O(n)       | O(n^2)     | O(n^2)     | O(1)   | Yes    |
| Counting sort  | O(n+k)     | O(n+k)     | O(n+k)     | O(k)   | Yes    |
| Linear search  | O(1)       | O(n)       | O(n)       | O(1)   | —      |
| Binary search  | O(1)       | O(log n)   | O(log n)   | O(1)   | —      |

## Graph algorithms

| Algorithm          | Time            | Space      | Notes                              |
|--------------------|-----------------|------------|------------------------------------|
| BFS / DFS          | O(V + E)        | O(V)       | Unweighted shortest path = BFS     |
| Dijkstra (heap)    | O((V+E) log V)  | O(V)       | Non-negative weights               |
| Bellman-Ford       | O(V·E)          | O(V)       | Handles negative edges             |
| Floyd-Warshall     | O(V^3)          | O(V^2)     | All-pairs shortest paths           |
| Topological sort   | O(V + E)        | O(V)       | DAGs only                          |
| Union-Find         | ~O(α(n)) ≈ O(1) | O(n)       | With path compression + union rank |

## Tree heights / structures

| Structure        | Search     | Insert     | Delete     | Notes                    |
|------------------|------------|------------|------------|--------------------------|
| BST (balanced)   | O(log n)   | O(log n)   | O(log n)   | AVL, Red-Black           |
| BST (worst)      | O(n)       | O(n)       | O(n)       | Degenerate skew          |
| Heap (binary)    | O(n)       | O(log n)   | O(log n)   | min/max in O(1)          |
| Trie             | O(L)       | O(L)       | O(L)       | L = key length           |
| Hash table       | O(1) avg   | O(1) avg   | O(1) avg   | O(n) worst on collision  |

## Recursion gotchas
- Default Python recursion limit ≈ 1000. `sys.setrecursionlimit(10**6)` if needed.
- Each call ≈ 80–100 bytes of stack — deep recursion can stack-overflow before it gets slow.
- Tail recursion is NOT optimized in Python — convert to iteration when depth grows with n.
