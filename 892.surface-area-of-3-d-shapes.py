#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        zeros_cnt = 0
        for r in range(n):
            for c in range(n):
                left,right,up,down=0,0,0,0
                if grid[r][c]==0: zeros_cnt += 1
                if c-1>=0:
                    left = max(grid[r][c]-grid[r][c-1],0)
                else:
                    left = grid[r][c]
                
                if c+1<n:
                    right = max(grid[r][c]-grid[r][c+1],0)
                else:
                    right = grid[r][c]
                
                if r-1>=0:
                    up = max(grid[r][c]-grid[r-1][c],0)
                else:
                    up = grid[r][c]
                
                if r+1<n:
                    down = max(grid[r][c]-grid[r+1][c],0)
                else:
                    down = grid[r][c]
                
                area += sum([left,right,up,down])

        return area + n*n*2 - zeros_cnt*2
    
    
    ################### solution #################
        # n, res = len(grid), 0
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j]: res += 2 + grid[i][j] * 4
        #         if i: res -= min(grid[i][j], grid[i - 1][j]) * 2
        #         if j: res -= min(grid[i][j], grid[i][j - 1]) * 2
        # return res
# @lc code=end

