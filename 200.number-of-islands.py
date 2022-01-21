#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # NOTE: global paramters and sanity check
        ROWS, COLS = len(grid), len(grid[0])
        if ROWS == 0: return 0
        # NOTE: expected answer
        num_island = 0
        ##################### DFS #######################

        
        # def dfs(row,col):
        #     grid[row][col] = 0
        #     for r, c in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
        #         if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1":
        #             dfs(r,c)
                    
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if grid[row][col] == "1":
        #             num_island += 1
        #             dfs(row,col)
        # return num_island
        
        # # time O(mn) | space O(mn)
        
        
        
        ###################### BFS ###########################
        for row_ in range(ROWS):
            for col_ in range(COLS):
                if grid[row_][col_] == "1":
                    num_island += 1
                    grid[row_][col_] == 0
                    neighbors = collections.deque([(row_,col_)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for r, c in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
                            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1":
                                neighbors.append((r,c))
                                grid[r][c] = 0
        return num_island
            
        # time O(mn) | space O(min(m,n))
        
# @lc code=end

