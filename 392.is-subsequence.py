#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # # require in-order appearance
        if not len(s): return True
        if len(s) > len(t): return False
        p = 0
        for char in t:
            if p<len(s) and s[p] == char:
                p+=1
        return p==len(s)
        
# @lc code=end

