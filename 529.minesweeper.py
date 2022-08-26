#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # dfs solution
        m,n = len(board),len(board[0])
        r,c = click
        
            
# @lc code=end

