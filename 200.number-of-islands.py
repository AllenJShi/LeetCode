#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ########### bfs solution ##########
        # directions = ((1,0),(0,1),(-1,0),(0,-1))
        # res = 0
        # visited = set()
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c]=="0" or (r,c) in visited:
        #             continue
        #         queue = deque([(r,c)])
        #         while queue:
        #             i,j = queue.popleft()
        #             neighbors = [map(sum,zip((i,j),direction)) for direction in directions]
        #             for ii,jj in neighbors:
        #                 if 0<=ii<len(grid) and 0<=jj<len(grid[0]) and grid[ii][jj]=="1" and (ii,jj) not in visited:
        #                     queue.append((ii,jj))
        #                     visited.add((ii,jj))
        #         res += 1
        # return res
        # idea: optimize the space complexity by flipping "1" to "0"
        
        ############ dfs solution ##############
        if not grid:
            return 0
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
                
# @lc code=end

