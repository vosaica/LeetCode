#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        vertical = len(matrix)
        horizontal = len(matrix[0])
        result = []

        col = -1
        row = 0

        while True:
            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if dir[0] == 0:  # horizontal move
                    for _ in range(horizontal):
                        col += dir[1]
                        result.append(matrix[row][col])
                    vertical -= 1
                    if vertical == 0:
                        return result
                else:  # vertical move
                    for _ in range(vertical):
                        row += dir[0]
                        result.append(matrix[row][col])
                    horizontal -= 1
                    if horizontal == 0:
                        return result


# @lc code=end

print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
