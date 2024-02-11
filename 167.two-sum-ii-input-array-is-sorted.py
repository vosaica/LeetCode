#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i != j:
            sum = numbers[i] + numbers[j]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            else:
                return [i + 1, j + 1]
        return


# @lc code=end

print(Solution().twoSum([1, 2, 4, 5, 6, 7, 8, 9], 12))
