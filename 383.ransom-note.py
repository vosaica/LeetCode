#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        vocabs = {}
        for c in magazine:
            if c in vocabs:
                vocabs[c] += 1
            else:
                vocabs[c] = 1

        for c in ransomNote:
            if c not in vocabs or vocabs[c] <= 0:
                return False
            vocabs[c] -= 1

        return True


# @lc code=end
