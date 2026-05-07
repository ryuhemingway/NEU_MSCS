# LeetCode Practice

50 easy problems + 30 medium problems + cheat sheets, organized for offline practice.

```
LeetCode Problems/
├── README.md             ← you are here
├── cheatsheets/
│   ├── 01_big_o.md
│   ├── 02_python_collections.md
│   ├── 03_patterns.md
│   └── 04_complexity_and_constraints.md
├── easy/                 (50 problems)
└── medium/               (30 problems)
```

Each problem file has the question + a hint at the top, an empty stub to fill
in, and the full solution at the bottom commented out with `#`. Solve first,
then uncomment to compare.

---

## How to use this on a flight

1. **Warm up** by skimming `cheatsheets/03_patterns.md` once — even five
   minutes of "what does sliding window look like?" pays off.
2. **Drill one pattern at a time** using the index below. Doing all 6 sliding
   window problems back-to-back beats hopping around randomly.
3. **Read the constraints first** for each problem and predict the required
   complexity (`cheatsheets/04_complexity_and_constraints.md`). Most beginners
   skip this step and over-engineer.
4. **Time yourself loosely.** Easy = aim for 10–15 min, Medium = 20–30 min.
   If you're stuck after the time limit, peek at the solution, understand it,
   close the file, and try again from scratch the next day.

---

## Index by pattern

> `E##` = easy/##_*.py · `M##` = medium/##_*.py

### Arrays & Hashing
- E01 Two Sum · E07 Remove Duplicates from Sorted Array · E08 Remove Element
- E17 Merge Sorted Array · E21 Pascal's Triangle · E34 Contains Duplicate
- E35 Contains Duplicate II · E41 Valid Anagram · E42 Missing Number
- E43 Move Zeroes · E45 First Unique Character · E47 Intersection of Two Arrays II
- E48 Ransom Note · M12 Group Anagrams

### Two Pointers
- E23 Valid Palindrome · E44 Reverse String · E49 Two Sum II (sorted)
- M04 Container With Most Water · M05 3Sum · M19 Sort Colors

### Sliding Window
- M02 Longest Substring Without Repeating Characters

### Stack
- E05 Valid Parentheses · E26 Min Stack · E36 Stack from Queues
- E38 Queue from Stacks

### Binary Search
- E10 Search Insert Position · E14 Sqrt(x)
- M09 Search in Rotated Sorted Array · M10 First and Last Position

### Linked Lists
- E06 Merge Two Sorted Lists · E16 Remove Duplicates from Sorted List
- E25 Linked List Cycle · E27 Intersection of Two Linked Lists
- E30 Reverse Linked List · E32 Remove Linked List Elements
- E39 Palindrome Linked List
- M01 Add Two Numbers · M07 Remove Nth Node From End

### Trees (BFS / DFS / recursion)
- E18 Same Tree · E19 Symmetric Tree · E20 Maximum Depth · E37 Invert Binary Tree
- M22 Validate BST · M23 Level Order Traversal

### Backtracking
- M06 Letter Combinations of a Phone Number · M08 Generate Parentheses
- M11 Combination Sum · M20 Subsets · M21 Word Search

### Dynamic Programming
- E15 Climbing Stairs · E22 Best Time to Buy and Sell Stock
- M13 Maximum Subarray (Kadane) · M17 Unique Paths · M25 Word Break
- M27 House Robber

### Greedy
- M15 Jump Game · M24 Best Time to Buy and Sell Stock II

### Graphs / Topological Sort
- M28 Number of Islands · M29 Course Schedule

### Heap / Priority Queue
- M30 Kth Largest Element

### Hash Map / Hash Set Design
- M26 LRU Cache

### Intervals
- M16 Merge Intervals

### Matrix
- M14 Spiral Matrix · M18 Set Matrix Zeroes

### Bit Manipulation
- E24 Single Number · E40 Power of Two

### Math / Number
- E02 Palindrome Number · E12 Plus One · E13 Add Binary · E29 Excel Column Number
- E31 Happy Number · E46 FizzBuzz

### Strings
- E03 Roman to Integer · E04 Longest Common Prefix · E09 First Occurrence
- E11 Length of Last Word · E33 Isomorphic Strings
- M03 Longest Palindromic Substring

### Voting / Single-pass tricks
- E28 Majority Element (Boyer-Moore) · E50 Range Sum Query (prefix sum)

---

## Suggested 14-hour flight study order

If you're not sure where to start, this order builds skills cumulatively:

1. **Hour 1–2:** Read the cheat sheets. Don't skip.
2. **Hour 2–4:** Two pointers + sliding window — E23, E44, E49, M04, M05, M02.
3. **Hour 4–6:** Stack + binary search — E05, E26, E10, E14, M09, M10.
4. **Hour 6–8:** Linked lists end-to-end — E06, E16, E25, E27, E30, E39, M01, M07.
5. **Hour 8–10:** Trees + BFS/DFS — E18, E19, E20, E37, M22, M23, M28.
6. **Hour 10–12:** Backtracking — M06, M08, M11, M20, M21.
7. **Hour 12–14:** DP, then whatever feels weakest — E15, E22, M13, M17, M25, M27.

Skip any you've already mastered. Go back to the cheat sheets between
sections — they reinforce more than you'd think.

---

## How to think about a new problem

1. **Read constraints first.** Pick the target complexity from
   `04_complexity_and_constraints.md`.
2. **Pattern-match.** Use the table at the bottom of `03_patterns.md` to
   guess the technique. Most LC easies/mediums fit a small set of patterns.
3. **Try the brute force first**, even mentally. It establishes correctness
   and gives you a baseline to optimize.
4. **State the recurrence / invariant out loud** before coding. If you can't
   explain why your loop terminates / why your DP is right, the code won't
   work either.
5. **Trace a tiny example.** n=2 or n=3 catches off-by-one bugs immediately.
6. **Edge cases:** empty input, single element, duplicates, target absent,
   negative numbers, max-size input, recursion depth.

Have a good flight.
