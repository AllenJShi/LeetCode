#
# @lc app=leetcode id=343 lang=python
#
# [343] Integer Break
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i]：分拆数字i，可以得到的最大乘积为dp[i]。
        dp = [0]*(n+1)
        # 0和1不能拆分，所以保留0
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(2,i):
                dp[i] = max(dp[i],j*dp[i-j],j*(i-j))
        return dp[n]
        
# @lc code=end

