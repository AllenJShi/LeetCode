#
# @lc app=leetcode id=171 lang=python
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ans, multiplier = 0, 1
        # 从最后以为往前
        for idx in range(len(columnTitle)-1,-1,-1):
            val = ord(columnTitle[idx]) - ord('A') + 1
            ans += val*multiplier
            multiplier *= 26
        return ans
        
# @lc code=end

