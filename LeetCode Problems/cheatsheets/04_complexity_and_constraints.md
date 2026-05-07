# Picking an Approach from the Constraints

LeetCode (and most interviews) tell you the constraint sizes. Use them to back into the required complexity.

| n constraint        | Allowed complexity           | Likely techniques                          |
|---------------------|------------------------------|--------------------------------------------|
| n ≤ 10              | O(n!), O(2^n)                | brute force, backtracking, permutations    |
| n ≤ 20              | O(2^n) or O(n · 2^n)         | bitmask DP, subset enumeration             |
| n ≤ 500             | O(n^3)                       | Floyd-Warshall, interval DP                |
| n ≤ 5,000           | O(n^2)                       | DP, nested loops                           |
| n ≤ 10^5            | O(n log n)                   | sort, heap, segment tree, binary search    |
| n ≤ 10^6            | O(n) or O(n log log n)       | hashing, two pointers, sliding window      |
| n ≤ 10^8            | O(log n) or O(1)             | math, closed form, binary search           |

## Time budget
- Most LC judges allow ~10^8 simple ops/sec for compiled code, ~10^7 for Python.
- If your loop count × per-op cost exceeds that, find a better algorithm.

## Memory
- 256 MB ≈ 6×10^7 ints in Python.
- If a 2D dp[n][n] won't fit (n ≈ 10^4), reduce to rolling row(s).

## Common rewrites

| Brute force         | Better                                         |
|---------------------|------------------------------------------------|
| O(n^2) two-loop search   | hash map (one pass)                       |
| O(n^2) sort + scan       | binary search after sort                  |
| Recursion + repeated subproblems | memoization (top-down DP)         |
| Recompute window sum every step  | sliding window with running sum   |
| Repeated range sum queries       | prefix sum array                  |
| Nested "for each pair" check     | sort then two-pointer             |
| Find min repeatedly      | heap                                      |
| "Have I seen this state?" | hash set                                 |

## Edge cases checklist
Run mentally through these before submitting:
- Empty input (`[]`, `""`)
- Single element
- All elements the same
- Already sorted / reverse sorted
- Negatives / zeros mixed in
- Duplicates
- Max-size input (overflow? recursion depth?)
- Target not present (return what?)
- Off-by-one on string/array indices
- Mutating input — does the caller expect that?
