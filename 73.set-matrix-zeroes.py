#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#

# @lc code=start

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ################## 我的答案 time O(mn) | space O(max(m,n)) ########
        # ROWS, COLS = len(matrix), len(matrix[0])
        # arr  = []
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if matrix[row][col] == 0:
        #             arr.append((row,col))
        
        # for (i,j) in arr:
        #     matrix[i] = [0 for _ in range(COLS)]
        #     for r in range(ROWS):
        #         matrix[r][j] = 0
                
        ############## 参考答案 ###############
        ###### 方法一：
        ROWS, COLS = len(matrix), len(matrix[0])
        row_arr, col_arr = [False]*ROWS, [False]*COLS
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    row_arr[row] = col_arr[col] = True
        
        for i in range(ROWS):
            for j in range(COLS):
                if row_arr[i] or col_arr[j]:
                    matrix[i][j] = 0
                    
        # time O(mn) | space O(m+n)
                              
                              
        ########## 方法二：
        # ROWS, COLS = len(matrix), len(matrix[0])
        # flag_col0 = any(matrix[i][0]==0 for i in range(ROWS))
        # flag_row0 = any(matrix[0][j]==0 for j in range(COLS))
        
        # for row in range(1, ROWS):
        #     for col in range(1, COLS):
        #         if matrix[row][col] == 0:
        #             matrix[row][0] = matrix[0][col] = 0

        # for i in range(1,ROWS):
        #     for j in range(1,COLS):
        #         if matrix[i][0] == 0 or matrix[0][j] == 0:
        #             matrix[i][j] = 0
        
        # if flag_col0:
        #     for i in range(ROWS):
        #         matrix[i][0] = 0
        
        # if flag_row0:
        #     for j in range(COLS):
        #         matrix[0][j] = 1
        
        # time O(mn) | space O(1)
                
# @lc code=end

