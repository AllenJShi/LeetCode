#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ################### BRUTE FORCE - TIME O(N^2) SPACE O(1) ##################
        """
        maxProfit = 0
        for i in range(len(prices)-1):
            for j in range(i,len(prices)):
                maxProfit = max(maxProfit, prices[j] - prices[i])
        
        return maxProfit
        
        """
        ################## TIME O(N) SPACE O(1) #######################
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit, price-minPrice)
            minPrice = min(minPrice, price)
        return maxProfit
            
# @lc code=end

