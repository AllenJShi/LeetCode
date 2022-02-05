#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
    #     if n < 2:
    #         return n
        
    #     dp = [0]*(n+1)
    #     dp[0] = 1
    #     # dp[1] = 1
    #     # dp[2] = 2
        
    #     # for i in range(3,n+1):
    #     #     dp[i] = dp[i-1] + dp[i-2]
                
    #     for i in range(n+1):
    #         for j in range(1,3):
    #             if i>=j:
    #                 dp[i] += dp[i-j]
        
    #     return dp[-1]
    # # NOTE：dp最后就是一个斐波那契数列
    
        ########### 我的答案 ############
        if n < 2: return n
        dp = [0] * (n+1)
        # dp[0]代表在第0层的方法，不加入讨论，因为n为正数
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
# @lc code=end

