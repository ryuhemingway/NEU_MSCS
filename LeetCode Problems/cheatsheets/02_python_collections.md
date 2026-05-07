# Python Collections Quick Reference

## list
```python
a = [1, 2, 3]
a.append(4)         # [1,2,3,4]
a.extend([5, 6])    # [1,2,3,4,5,6]
a.insert(0, 0)      # O(n) — avoid in hot loops
a.pop()             # 6, list now [...5]
a.pop(0)            # O(n)
a.remove(3)         # removes first occurrence of value 3, O(n)
a.index(2)          # first index of value 2, O(n)
a.count(2)          # how many 2s, O(n)
a.reverse()         # in-place, O(n)
a.sort()            # in-place, O(n log n) — stable
sorted(a, key=lambda x: -x, reverse=False)
a[::-1]             # reversed copy
a[2:5]              # slice
a[::2]              # every other element
```

## dict
```python
d = {}
d['k'] = 1
d.get('k', 0)              # returns 0 if missing — never KeyError
d.setdefault('list', []).append(x)   # init-and-append idiom
d.pop('k', None)           # remove with default
d.keys() / d.values() / d.items()
'k' in d                   # O(1)
{k: v for k, v in pairs}   # comprehension

from collections import defaultdict
groups = defaultdict(list)
groups[key].append(val)    # no setdefault dance needed
```

## set
```python
s = set()
s.add(x); s.discard(x)     # discard never raises; remove does
s & t   # intersection
s | t   # union
s - t   # difference
s ^ t   # symmetric difference
frozenset(...)             # hashable, can be a dict key
```

## collections.Counter
```python
from collections import Counter
c = Counter("aabbbc")              # {'a':2, 'b':3, 'c':1}
c.most_common(2)                   # [('b',3),('a',2)]
c1 + c2                            # add counts (drops <=0)
c1 - c2                            # subtract (drops <=0)
c1 & c2                            # min counts (multiset intersection)
c1 | c2                            # max counts
```

## collections.deque (double-ended queue)
```python
from collections import deque
q = deque([1, 2, 3])
q.append(4); q.appendleft(0)       # O(1) on both ends
q.pop(); q.popleft()               # O(1) on both ends
q.rotate(1)                        # right-rotate — useful tricks
deque(maxlen=k)                    # auto-evicts oldest — sliding window
```

## heapq (min-heap)
```python
import heapq
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappop(h)            # 1
heapq.heappushpop(h, 3)     # push then pop in one step (faster)
heapq.heapify(arr)          # in-place, O(n)
heapq.nlargest(k, iter)     # top-k
heapq.nsmallest(k, iter)
# max-heap: negate the keys, or push tuples (-priority, item)
```

## bisect (binary search on sorted list)
```python
import bisect
i = bisect.bisect_left(arr, x)     # leftmost position where x fits
i = bisect.bisect_right(arr, x)    # rightmost position
bisect.insort(arr, x)              # insert keeping sorted, O(n) due to shift
```

## itertools (combinatorics + iteration)
```python
from itertools import (
    permutations, combinations, combinations_with_replacement,
    product, accumulate, chain, groupby, count, cycle, islice
)
list(permutations([1,2,3], 2))       # P(3,2)
list(combinations([1,2,3], 2))       # C(3,2)
list(product([0,1], repeat=3))       # cartesian product (binary masks)
list(accumulate([1,2,3,4]))          # [1,3,6,10] — prefix sums
chain([1,2],[3,4])                   # flatten one level
```

## String idioms
```python
s.lower() / s.upper() / s.swapcase()
s.strip() / s.lstrip() / s.rstrip()
s.split() / s.split(',') / ' '.join(parts)
s.startswith(p) / s.endswith(p)
s.find('x')                # -1 if not found (vs index() which raises)
s.replace('a', 'b')
s.isalnum() / .isalpha() / .isdigit() / .isspace()
ord('a')  # 97
chr(97)   # 'a'
'abc'[::-1]                # 'cba'
```

## Useful built-ins
```python
enumerate(seq, start=0)
zip(a, b)                  # stops at shortest
zip(*matrix)               # transpose: rows -> cols
list(zip_longest(a, b, fillvalue=0))   # itertools
any(x > 0 for x in arr)
all(x > 0 for x in arr)
sum(arr) / min(arr) / max(arr)
min(arr, key=lambda x: x.cost)
divmod(17, 5)              # (3, 2)
```

## Initialize 2D grids correctly
```python
# Wrong (all rows share the same list):
grid = [[0] * cols] * rows

# Right:
grid = [[0] * cols for _ in range(rows)]
```
