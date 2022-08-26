#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # ################# bfs solution (TLE) #####################
        # directions = [(1,0),(0,1),(-1,0),(0,-1)]
        # pacific = set()
        # atlantic = set()
        # m,n = len(heights),len(heights[0])
        
        # # only need to bfs on four edges
        # def bfs(r,c,visited):
        #     if (r,c) in visited: return
        #     queue = deque([(r,c)])
        #     visited.add((r,c))
        #     while queue:
        #         ri,ci = queue.popleft()
        #         visited.add((ri,ci))
        #         for direction in directions:
        #             ii, jj = tuple(map(sum,zip(direction,(ri,ci))))
        #             if 0<=ii<m and 0<=jj<n and (ii,jj) not in visited:
        #                 # if the neighboring height greater than current height
        #                 # this means the current height reachable from neighboring
        #                 # inner neighbor higher than outter current
        #                 if heights[ii][jj] >= heights[ri][ci]:
        #                     queue.append((ii,jj))
        
        # # maintain visited sets
        # # first, check left and right edges
        # for r in range(m):
        #     # col = 0
        #     bfs(r,0,pacific)                 
        #     # col = n-1
        #     bfs(r,n-1,atlantic)
        # # second, check top and bottom edges
        # for c in range(n):
        #     # row = 0
        #     bfs(0,c,pacific)                 
        #     # row = m-1
        #     bfs(m-1,c,atlantic)

        # return list(pacific & atlantic)
        
        
                
        ################# dfs solution ###################
        if not heights: return heights
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        m,n = len(heights),len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(i,j,visited):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for direction in directions:
                ii,jj = tuple(map(sum,zip((i,j),direction)))
                # if (ii,jj) within the grid
                if 0<=ii<m and 0<=jj<n:
                    # if neighboring height greater than current height 
                    if heights[ii][jj] >= heights[i][j]:
                        dfs(ii,jj,visited)
        
        # run dfs from boundaries toward the center
        # maintain the visited sets for all heights reachable from boundaries
        for r in range(m):
            # run dfs on left edge (pacific)
            dfs(r,0,pacific)
            # run dfs on right edge (atlantic)
            dfs(r,n-1,atlantic)
            
        for c in range(n):
            # run dfs on top edge (pacific)
            dfs(0,c,pacific)
            # run dfs on bottom edge (atlantic)
            dfs(m-1,c,atlantic)
            
        # return union of pacific and atlantic
        return list(pacific & atlantic)
            
        
        
        
# @lc code=end

