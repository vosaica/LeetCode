#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def helper(self, s: str, i: int, j: int) -> bool:
        if i >= j:
            return True

        if not s[i].isalnum():
            return self.helper(s, i + 1, j)
        elif not s[j].isalnum():
            return self.helper(s, i, j - 1)
        elif i + 1 == j:
            return s[i].lower() == s[j].lower()
        elif s[i].lower() == s[j].lower():
            return self.helper(s, i + 1, j - 1)
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        return self.helper(s, 0, len(s) - 1)


a = Solution()
print(a.isPalindrome("0P"))
# @lc code=end
