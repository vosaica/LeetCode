#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    isValidSudoku = lambda _, board: all(not any((lambda s, view: any((c in s or s.add(c)) for c in view))(set(), view) for view in views) for views in ([[c for c in row if c != "."] for row in board], [[row[i] for row in board if row[i] != "."] for i in range(0, 9)], [[board[row + i][col + j] for j in range(3) for i in range(3) if board[row + i][col + j] != "."] for row in range(0, 9, 3) for col in range(0, 9, 3)]))  # noqa: E731

# @lc code=end

print(
    Solution().isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
