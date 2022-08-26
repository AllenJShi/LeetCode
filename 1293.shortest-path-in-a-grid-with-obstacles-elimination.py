#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        # base case
        if m==n==1: return 0
        if k > m-1+n-1: return m-1 + n-1
        # use a queue to store (row,col,k_left,steps)
        queue = deque([(0,0,k,0)])
        # use a set to store (r,c,k_left)
        visited = set([(0,0,k)])
        directions = ((0,1),(1,0),(-1,0),(0,-1))
        
        while queue:
            r,c,k_left,steps = queue.popleft()
            for ri,ci in [tuple(map(sum,zip((r,c),direction))) for direction in directions]:
                if 0<=ri<m and 0<=ci<n:
                    # if on a block and with k left
                    if grid[ri][ci] and k_left>0 and (ri,ci,k_left-1) not in visited:
                        visited.add((ri,ci,k_left-1))
                        queue.append((ri,ci,k_left-1,steps+1))
                    # if on empty
                    elif not grid[ri][ci] and (ri,ci,k_left) not in visited:
                        # assumption: the last block is empty; otherwise, need to check if k_left>0
                        if ri==m-1 and ci==n-1:
                            return steps+1
                        visited.add((ri,ci,k_left))
                        queue.append((ri,ci,k_left,steps+1))
        return -1
# @lc code=end

