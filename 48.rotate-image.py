#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # # 每一行变成列，并且第一行变成最后一列
        # for row in range(ROWS//2):
        #     for col in range((COLS+1)//2):
        #         matrix[row][col],matrix[COLS-col-1][row],\
        #             matrix[COLS-row-1][ROWS-col-1], matrix[col][ROWS-row-1]  \
        #                 = matrix[COLS-col-1][row], matrix[COLS-row-1][ROWS-col-1], \
        #                     matrix[col][ROWS-row-1], matrix[row][col]
        
        
        # 水平翻转，沿对角线翻转
        for row in range(ROWS//2):
            for col in range(COLS):
                matrix[row][col], matrix[ROWS-row-1][col]\
                    = matrix[ROWS-row-1][col], matrix[row][col]
        for i in range(ROWS):
            for j in range(i):
                matrix[i][j], matrix[j][i] \
                    = matrix[j][i], matrix[i][j]
        
# @lc code=end

