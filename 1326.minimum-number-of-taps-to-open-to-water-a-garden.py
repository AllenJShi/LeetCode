#
# @lc app=leetcode id=1326 lang=python
#
# [1326] Minimum Number of Taps to Open to Water a Garden
#

# @lc code=start
class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        ############### DP ################
        prev = [x for x in range(n+1)]
        for i in range(n+1):
            li = max(i-ranges[i],0)
            ri = min(i+ranges[i],n)
            prev[ri] = min(prev[ri],li)
            
        ############## 普通 DP 版##############
        # BIG = 2**30
        # dp = [0] + [BIG]*n
        # for i in range(1,n+1):
        #     for j in range(prev[i],i):
        #         if dp[j] != BIG:
        #             dp[i] = min(dp[i],dp[j]+1)
        # return -1 if dp[n] == BIG else dp[n]
    
        # time O(NR) | space O(N)
    
        ############## Gready 版 ##############
        breakpoint, furthest = n, 2**30
        ans = 0
        for i in range(n,0,-1):
            furthest = min(furthest,prev[i])
            if i == breakpoint:
                if furthest >= i:
                    return -1
                breakpoint = furthest
                ans += 1
        return ans
    
        # time O(N) | space O(N)
        
# @lc code=end

