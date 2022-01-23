#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #################### 我的答案 ######################
        ROWS, COLS = len(grid), len(grid[0])
        # print(ROWS,COLS)
        dp = [[float('inf')]*COLS for _ in range(ROWS)]
        
        dp[0][0] = grid[0][0]
        
        # 若 n x 1 或 1 x n 的矩阵，只有一个方向可以选择
        if ROWS==1 or COLS==1: return sum(*grid)
        
        for row in range(ROWS):
            for col in range(COLS):
                if row+1 < ROWS and col+1<COLS:
                    dp[row+1][col] =\
                        min(dp[row+1][col],dp[row][col]+grid[row+1][col])
                    # print(dp)
                    dp[row][col+1] =\
                        min(dp[row][col+1],\
                            dp[row][col]+grid[row][col+1])
                else:
                    ## the last col and row
                    dp[row][col] =\
                        min(dp[row-1][col],dp[row][col-1])+grid[row][col]
        print(dp)
        return dp[ROWS-1][COLS-1]
        
# @lc code=end

