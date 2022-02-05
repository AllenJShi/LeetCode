#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        ####################### 我的答案 ####################
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (COLS) for _ in range(ROWS)]
        for i in range(COLS):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        
        for i in range(ROWS):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
            
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        
        
        ########################################
        print_(obstacleGrid)
        
        
        print("+++++++++++++++++++++++++++++++++++")
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==1:
                break
            f[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i]==1:
                break
            f[0][i] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    continue
                    # f[i][j] = 0
                # if j-1>=0 and obstacleGrid[i][j]==0:
                f[i][j] = f[i-1][j] + f[i][j-1]
                    
                    
        print_(f)
        return f[m-1][n-1]
        
def print_(mat):
    for i in mat:
        print(i)
        
        
        
        
        
# @lc code=end

