#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # val = image[sr][sc]
        # directions = ((1,0),(0,1),(-1,0),(0,-1))
        # visited = set([(sr,sc)])
        # def dfs(r,c):
        #     if not (0<=r<len(image) and 0<=c<len(image[0])):
        #         return
        #     image[r][c] = color
        #     for r_,c_ in [map(sum,tuple(zip((r,c),direction))) for direction in directions]:
        #         if 0<=r_<len(image) and 0<=c_<len(image[0]) and image[r_][c_]==val and (r_,c_) not in visited: 
        #             visited.add((r_,c_))
        #             dfs(r_,c_)
        #         else:
        #             continue
        # dfs(sr,sc)
        # return image
            
            
        xlen = len(image)
        ylen = len(image[0])
        ori = image[sr][sc]
        
        def dfs(x, y):
            if 0<=x<xlen and 0<=y<ylen and image[x][y]==ori:
                image[x][y] = color
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
    
        if ori != color:
            dfs(sr, sc)
        return image
        
        
# @lc code=end

