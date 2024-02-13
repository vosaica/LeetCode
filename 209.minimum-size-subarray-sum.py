#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
import math


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = math.inf

        i = 0
        j = 0
        sum = 0
        while j < len(nums):
            sum += nums[j]
            if sum >= target:
                res = min(res, j - i + 1)
                while True:
                    if sum - nums[i] >= target:
                        sum -= nums[i]
                        i += 1
                        res = min(res, j - i + 1)
                    else:
                        break
            j += 1

        return int(res) if math.isfinite(res) else 0


# @lc code=end

print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
