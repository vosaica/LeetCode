#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        count = 1
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                count = 1
                i += 1
                nums[i] = nums[j]
            elif count < 2:
                count += 1
                i += 1
                nums[i] = nums[j]
        return i + 1


Solution().removeDuplicates([1, 2, 2, 3, 4, 5, 5])
# @lc code=end
