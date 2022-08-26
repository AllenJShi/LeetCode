#
# @lc app=leetcode id=1871 lang=python3
#
# [1871] Jump Game VII
#

# @lc code=start
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        cnt = 1 # number of reachable points within the sliding window 
        for i in range(minJump,n): # from minJump to n-1
            if s[i] == "0" and cnt > 0:
                # if reachable (cnt>0, more than none reachable points in window)
                # if i jumpable to next ("0")
                dp[i] = True
                
            if i >= maxJump and dp[i-maxJump]:
                # if i is out of 1st window
                # and prior farthest point is reachable
                # ie. the newly removed leftmost point is reachable
                cnt -= 1
            
            if dp[i-minJump+1]:
                # if cloest previous point is reachable
                # ie. the newly added rightmost point is reachable
                cnt += 1
            
        return dp[n-1]
    

# @lc code=end

