#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # if n < 2: return n
        # p, q, r = 0, 0, 1
        # for i in range(2,n+1):
        #     p, q = q, r
        #     r = p + q
        # return r 
        
        
        ############## 递归 ##############
        if n < 2: return n
        return self.fib(n-1) + self.fib(n-2)
        
        
        ############## DP ##################
        if n <= 1: return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]        
        return dp[-1]
        
# @lc code=endc

