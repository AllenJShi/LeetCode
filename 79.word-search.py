#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        path = set()
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            # 终止条件1：整个word都被遍历
            if i==len(word):
                return True
            # 终止条件2：board遍历完，或，当下的字母不对，或，board中的位置已经被游历
            if r<0 or c<0 or r>=ROWS or c>=COLS or word[i]!=board[r][c] or (r,c) in path:
                return False
            
            # 若没有终止，将该单元格记录
            path.add((r,c))
            # 查询相邻单元格，任何一个相邻格为true，即满足条件
            res = (dfs(r+1,c,i+1) or
                   dfs(r,c+1,i+1) or
                   dfs(r-1,c,i+1) or
                   dfs(r,c-1,i+1) )
            # 撤销回溯
            path.remove((r,c))
            return res
        
        # 遍历所有单元格作为起始位置
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False
        
        # Time O(n*m*4^n)
        
# @lc code=end

