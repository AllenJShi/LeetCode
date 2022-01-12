#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        MAX_LEN = 1
        # start = 0
        leftmost = 0
        rightmost = 0
        
        for i in range(n):
            dp[i][i] = True
        
        for j in range(1,n):
            for i in range(0,j):
                # if s[i] != s[j]:
                #     dp[i][j] = False
                # else:
                #     if j-i < 3:
                #         dp[i][j] = True
                #     else:
                #         dp[i][j] = dp[i+1][j-1]
                        
                # if dp[i][j] and j-i+1 > MAX_LEN:
                #     MAX_LEN = j-i+1
                #     start = i
        # return s[start:start+MAX_LEN]
                if s[i] == s[j] and (dp[i+1][j-1] or j-i<3):
                    dp[i][j] = True
                    if j-i+1 > MAX_LEN:
                        MAX_LEN = j-i+1
                        leftmost = i
                        rightmost = j
                
        return s[leftmost:rightmost+1]
        
        
# @lc code=end

