#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
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

