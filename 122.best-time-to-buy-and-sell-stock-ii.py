#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ############### 贪心 ##################
        n = len(prices)
        ans = 0
        
        # 若当天的盈利大于前一天的最大盈利，
        # 前一天卖出后，第二天买入，结束时卖出
        # 若当天盈利为负数
        # 则不买入该股，当天为止最大盈利即为前一天的最大盈利
        for i in range(1,n):
            ans += max(0,prices[i]-prices[i-1])
        return ans
    
        # time O(n) | space O(1)
    

        ###############`动态规划 ###############
        # n = len(prices)
        # dp = [[0] * n for _ in range(2)]
        # dp[0][0] = 0
        # dp[1][0] = -prices[0]
        
        # for i in range(1,n):
        #     dp[0][i] = max(dp[0][i-1], dp[1][i-1]+prices[i])
        #     dp[1][i] = max(dp[1][i-1], dp[0][i-1]-prices[i])
        
        # return dp[0][n-1]
    
        # # time O(n) | space O(n) -> O(1)当只保留前一个dp0，dp1时
# @lc code=end

