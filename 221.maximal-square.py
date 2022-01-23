#
# @lc app=leetcode id=221 lang=python
#
# [221] Maximal Square
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 对每一个位置作为正方形右下角，向左上搜索最大的面积
        import numpy as np
        print(np.matrix(matrix))
        ROWS, COLS = len(matrix), len(matrix[0])
        if ROWS==0 or COLS==0: return 0
        maxStride = 0
        dp = [[0]*COLS for _ in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxStride = max(maxStride, dp[i][j])
        return maxStride**2
    
        # time O(mn) | space O(mn)
# @lc code=end

