#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            grid[i][j] = 0
            cnt = 1
            for dx,dy in dir:
                i_ = i + dx
                j_ = j + dy
                if 0 <= i_ < nrows and 0 <= j_ < ncols and grid[i_][j_] == 1:
                    cnt += dfs(i_,j_)
            return cnt
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        nrows,ncols = len(grid), len(grid[0])
        res = 0
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    res = max(dfs(r,c),res)
        return res
# @lc code=end

