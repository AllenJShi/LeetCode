#
# @lc app=leetcode id=746 lang=python
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # n = len(cost)
        # if n <=1:
        #     return n
        
        # dp = [0] * (n+1)
        # # dp[0] = cost[0]
        # # dp[1] = cost[1]
        
        # # for i in range(2,n):
        # #     dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            
        # # return min(dp[n-1],dp[n-2])
        
        # for i in range(2,n+1):
        #     dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
            
        # return dp[n]
        
        
        
        ############## 我的答案 #################
        n = len(cost)
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]
        
        
# @lc code=end

