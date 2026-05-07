"""
Problem 79: Word Search (Medium)

Given an m x n grid of characters `board` and a string `word`, return True if
`word` exists in the grid by moving sequentially through adjacent cells
(horizontally or vertically). The same cell may not be used more than once.

Example:
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "ABCCED"   -> True
    word = "ABCB"     -> False

Hint: DFS + backtracking from each cell. Mark visited by mutating the cell
(e.g., set to '#') and restore on the way back to keep O(1) extra space.
"""


def exist(board, word):
    # Your solution here
    pass


# ---------- Answer below (don't peek!) ----------
# def exist(board, word):
#     rows, cols = len(board), len(board[0])
#     def dfs(r, c, i):
#         if i == len(word):
#             return True
#         if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
#             return False
#         saved = board[r][c]
#         board[r][c] = '#'
#         found = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1)
#                  or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
#         board[r][c] = saved
#         return found
#     return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
