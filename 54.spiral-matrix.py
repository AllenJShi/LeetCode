#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        
        constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 10
        -100 <= matrix[i][j] <= 100
        """
        ################# 模拟 time O(mn) | space O(mn) ##############
        # ROWS, COLS = len(matrix), len(matrix[0])
        # total = ROWS * COLS
        # direction = [
        #     [0,1],
        #     [1,0],
        #     [0,-1],
        #     [-1,0]
        # ]
        # visited = [[False] * COLS for _ in range(ROWS)]
        # row = col = 0
        # directionIdx = 0
        # ans = [0] * total
        # for i in range(total):
        #     ans[i] = matrix[row][col]
        #     visited[row][col] = True
        #     [nextRow, nextCol] = [a+b for a,b in zip([row,col], direction[directionIdx])] 
        #     if not (0<=nextRow<ROWS and 0<=nextCol<COLS and not visited[nextRow][nextCol]):
        #         directionIdx = (directionIdx+1) % 4
        #     [row,col] = [a+b for a,b in zip([row,col], direction[directionIdx])] 
        # return ans
       
        
        
        ################ 逐层模拟 time O(mn) | space O(1) #########################
        ROWS, COLS = len(matrix), len(matrix[0])
        ans = []
        left, right, top, bottom = 0, COLS-1, 0, ROWS-1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                ans.append(matrix[left][col])
                
            for row in range(top+1, bottom+1):
                ans.append(matrix[row][right])
                
            if left < right and top < bottom:
                for col in range(right-1,left,-1):
                    ans.append(matrix[bottom][col])
                for row in range(bottom,top,-1):
                    ans.append(matrix[row][left])
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return ans
# @lc code=end

