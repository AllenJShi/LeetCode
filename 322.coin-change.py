#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ###################### DP #######################
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x],dp[x-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
        
        # time O(len(coins)*amount) | space O(amount + 1)
        
        ################# 回溯 ################
        def backtracking(remain):
            if remain < 0: return -1
            if remain == 0: return 0
            mini = int(1e9)
            for coin in coins:
                res = backtracking(remain-coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1
        if amount < 1: return 0
        return backtracking(amount)
    
        # time O(len(coins)*amount) | space O(amount + 1)
# @lc code=end

