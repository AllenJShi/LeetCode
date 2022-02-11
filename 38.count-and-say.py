#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#

# @lc code=start
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1: return '1'
        rec = self.countAndSay(n-1)
        ans = ''
        for n, reps in itertools.groupby(rec):
            ans += str(len(list(reps))) + n        
        return ans
               
        
# @lc code=end

