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
        # if n==1: return '1'
        # rec = self.countAndSay(n-1)
        # ans = ''
        # for n, reps in itertools.groupby(rec):
        #     ans += str(len(list(reps))) + n        
        # return ans
        
        def helper(n):
            if n==1: return "1"
            s = self.countAndSay(n-1)
            count = 0
            result = ''
            l = len(s)
            for i in range(l):
                count += 1
                if i==l-1 or s[i] != s[i+1]:
                    result += str(count) + str(s[i])
                    count = 0
            return result
        return helper(n)
# @lc code=end

