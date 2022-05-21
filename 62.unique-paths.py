#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """f(i,j) be the unique path to (i,j)
        f(i,j) = f(i-1,j) + f(i,j-1)
        f(0,0) = 1
        f(i,0) = 1
        f(0,j) = 0
        find(m-1,n-1)
        """
        
        ############# 我的答案 ############
        # dp = [[0]*n for _ in range(m)]
        # for i in range(m):
        #     dp[i][0] = 1
        # for j in range(n):
        #     dp[0][j] = 1
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[m-1][n-1]
    
        ######### dfs （超时）
        # def dfs(i,j):
        #     if i > m  or j > n: return 0
        #     if i==m and j==n: return 1
        #     return dfs(i+1,j) + dfs(i,j+1)
        # return dfs(1,1)
    
        
        f = [[1] * n] + [[1] + [0] * (n-1) for _ in range(m-1)]                
        for i in range(1,m):
            for j in range(1,n):
                f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m-1][n-1]
    
def print_(mat):
    for i in mat:
        print(i)
# @lc code=end

