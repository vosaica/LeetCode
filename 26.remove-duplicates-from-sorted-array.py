#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        largest = nums[0]
        i = 1
        for j in range(1, len(nums)):
            if nums[j] > largest:
                nums[i] = nums[j]
                largest = nums[j]
                i += 1
        return i


a = Solution()
Solution.removeDuplicates(a, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

# @lc code=end