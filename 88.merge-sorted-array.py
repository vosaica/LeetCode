#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# [1,2,6,8,0,0,0]

# [1,2,6,8,0,0,0]
#    ^
# [2,5,7]
#    ^

# @lc code=start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1c = nums1.copy()
        i = 0
        i1 = 0
        i2 = 0

        while i < m + n:
            if i1 == m:
                while i2 < n:
                    nums1[i] = nums2[i2]
                    i2 += 1
                    i += 1
                return
            if i2 == n:
                while i1 < m:
                    nums1[i] = nums1c[i1]
                    i1 += 1
                    i += 1
                return

            if nums1c[i1] < nums2[i2]:
                nums1[i] = nums1c[i1]
                i1 += 1
                i += 1
            else:
                nums1[i] = nums2[i2]
                i2 += 1
                i += 1

        """
        Do not return anything, modify nums1 in-place instead.
        """


# @lc code=end

n1 = [1, 2, 3, 0, 0, 0]
n2 = [2, 5, 6]

a = Solution()
a.merge(n1, 3, n2, 3)
print(n1)
