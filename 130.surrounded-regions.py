#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
                
        def dfs(i,j):
            if i in range(0,m) and j in range(0,n) and board[i][j] == 'O':
                board[i][j] = 'A'
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)

        # check the left and right col
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
          
        # check the top and bottom row  
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
        
                
                    
# @lc code=end

