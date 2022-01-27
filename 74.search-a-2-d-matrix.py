#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ############ 暴力法 ###############
        # ROWS, COLS = len(matrix), len(matrix[0])
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         val = matrix[i][j]
        #         if val == target: 
        #             return True
        #         elif val > target:
        #             return False
    
        # time O(n^2) | space O(1)
                
        # ######## 思路：每一row可以看作一个range，每次看target是否在range中，
        # ############## 若是，则在其中查找；若不是，跳到下一行或退出
        # ROWS, COLS = len(matrix), len(matrix[0])
        # i, j = 0, 0
        # while i+1 < ROWS and not (matrix[i][0] <= target <= matrix[i][COLS-1]):
        #     i += 1
        # while j < COLS:
        #     print(i,j)
        #     if matrix[i][j] == target:
        #         return True
        #     j += 1
        # return False
        # # time O(n) | space O(1)
        
        ############### 参考答案 ###############
        # ############## 两次二分
        # def binarySearchFirstColumn():
        #     low = -1
        #     high = len(matrix)-1
        #     while low < high:
        #         mid = (high - low + 1) / 2 + low
        #         if matrix[mid][0] <= target:
        #             low = mid
        #         else:
        #             high = mid - 1
        #     return low
        
        # def binarySearchRow(row):
        #     low, high = 0, len(row)-1
        #     # 此处需小于等于
        #     while low <= high:
        #         # mid的定义和之前不同
        #         mid = (high-low) / 2 + low
        #         if row[mid] == target:
        #             return True
        #         elif row[mid] > target:
        #             high = mid - 1
        #         else:
        #             low = mid + 1
        #     return False
        
        # rowIndex = binarySearchFirstColumn()
        # if rowIndex < 0:
        #     return False
        # else:
        #     return binarySearchRow(matrix[rowIndex])

        # time O(logmn) | space O(1)
        
        
        ############ 一次二分
        ROWS, COLS = len(matrix), len(matrix[0])
        low, high = 0, ROWS*COLS-1
        while low <= high:
            mid = (high-low) / 2 + low
            x = matrix[mid/COLS][mid%COLS]
            if x < target:
                low = mid + 1
            elif x > target:
                high = mid - 1
            else:
                return True
        return False
        
# @lc code=end

