#
# @lc app=leetcode id=240 lang=python
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        ROWS, COLS = len(matrix), len(matrix[0])
        # 从右上向左下进行搜索
        # 当前元素在当前row上处于最大，在当前col上是最小
        # 所以在发现target比元素小时，向左缩进col （同一row，使其变小）；
        # 反之，向下移动row（同一col，使其变大）
        x, y = 0, COLS-1
        while x < ROWS and y >= 0:
            # 若找到target，直接返回
            if matrix[x][y] == target:
                return True

            if matrix[x][y] > target:
                # 若当前元素大于target，说明target在左上
                y -= 1
            else:
                # 若当前元素小于target，证明target在右下
                x += 1     
        return False
        
# @lc code=end

