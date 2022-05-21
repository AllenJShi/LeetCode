#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        n = len(board)
        m = len(board[0])
        
        def neighbors(i,j):
            count = isLive(i+1,j)
            count += isLive(i-1,j)
            count += isLive(i,j+1)
            count += isLive(i,j-1)
            count += isLive(i-1,j-1)
            count += isLive(i-1,j+1)
            count += isLive(i+1,j-1)
            count += isLive(i+1,j+1)
            return count
            
        def isLive(i,j):
            if i<0 or i>=n or j<0 or j>=m: return 0
            # 0 means die, 5 means currently die but live next gen
            if board[i][j] == 0 or board[i][j] == 5: return 0
            return 1
        
        for i in range(n):
            for j in range(m):
                count = neighbors(i,j)
                # if i ,j  is live currently
                if board[i][j]:
                    # rule 1: less than 2 -> die by under-population
                    if count < 2:
                        board[i][j] = 2
                    # rule 2: 2 or 3 live to the next gen
                    elif count <= 3:
                        board[i][j] = 3
                    # rule 3: more than 3 -> die by over-population
                    else:
                        board[i][j] = 4
                # if i, j die currently but live to the next gen
                else:
                    # rule 4: exactly 3 and reproduction
                    if count == 3:
                        board[i][j] = 5
                        
        for i in range(n):
            for j in range(m):
                # die due to either over- or under-population
                if board[i][j] == 2 or board[i][j] == 4: board[i][j] = 0
                # live
                elif board[i][j] == 3 or board[i][j] == 5: board[i][j] = 1
        return
                
# @lc code=end

