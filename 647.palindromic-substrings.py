#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ############## 动态规划 ################
        
        # n = len(s)
        # dp = [[False]*n for _ in range(n)]
        # ans = 0
        # for j in range(n):
        #     for i in range(0,j+1):
        #         if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
        #             dp[i][j] = True
        #             ans += 1
        # return ans
        
        
        ########中间展开法
        ans = 0
        n = len(s)
        for center in range(2*n-1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left]==s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans 
        
        
        
        ##### 变化：只记录distinct
        # n = len(s)
        # dp = [[False]*n for _ in range(n)]
        # ans = 0
        # visited = []
        # for j in range(n):
        #     for i in range(0,j+1):
        #         if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
        #             dp[i][j] = True
        #             if s[i:j+1] in visited:
        #                 visited.append(s[i:j+1])
        #                 ans += 1
        # return ans
        
        
        
        
# @lc code=end

