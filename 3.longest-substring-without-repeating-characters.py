#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        i, j, ret = 0, 1, 1
        collection = set(s[i])

        while j < len(s):
            if s[j] in collection:
                while s[j] in collection:
                    collection.discard(s[i])
                    i += 1

            # s[i:j] should be valid substring at this point
            collection.add(s[j])
            ret = max(ret, j - i + 1)
            j += 1
        return ret


# @lc code=end

Solution().lengthOfLongestSubstring("au")
