#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # ################ bfs solution (TLE) ################
        # # this solution works but for testcase 49 TLE, but it illustrates good logic
        # m,n = len(mat),len(mat[0])
        # res = [[0 for _ in range(n)] for _ in range(m)]
        # directions = ((1,0),(-1,0),(0,1),(0,-1))
        # def bfs(r,c):
        #     # find the nearest 0
        #     queue = deque([((r,c),0)])
        #     visited = set()
        #     distance = 0
        #     while queue:
        #         for _ in range(len(queue)):
        #             pair,distance = queue.popleft()
        #             x,y = pair
        #             if mat[x][y]==0:
        #                 return distance
        #             visited.add(pair)
        #             for ri,ci in [tuple(map(sum,zip(pair,direction))) for direction in directions]:
        #                 if ri in range(0,m) and ci in range(0,n) and (ri,ci) not in visited:
        #                     queue.append(((ri,ci),distance+1))
        # for r in range(m):
        #     for c in range(n):
        #         if mat[r][c] == 1:
        #             distance = bfs(r,c)
        #             res[r][c] = distance
        # return res
        
        
        
        # # # a good idea: start the queue with all 0s
        # m,n = len(mat),len(mat[0])
        # res = [[inf for _ in range(n)] for _ in range(m)]
        # directions = ((1,0),(-1,0),(0,1),(0,-1))
        
        # queue = deque()
        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j]==0:
        #             queue.append((i,j))
        #             res[i][j] = 0
                    
        # while queue:
        #     pair = queue.popleft()
        #     neighbors = [tuple(map(sum,zip(pair,direction))) for direction in directions]
        #     for ri,ci in neighbors:
        #         if ri in range(m) and ci in range(n) and res[pair[0]][pair[1]]+1<res[ri][ci]:
        #             res[ri][ci] = res[pair[0]][pair[1]] + 1
        #             queue.append((ri,ci))
        
        # return res
        
        
        
        
        # dp solution
        m,n = len(mat),len(mat[0])
        res = [[inf for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i][j],res[i-1][j]+1)
                    if j > 0:
                        res[i][j] = min(res[i][j],res[i][j-1]+1)
        
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if mat[r][c]==0:
                    res[r][c] = 0
                else:
                    if r<m-1:
                        res[r][c] = min(res[r][c],res[r+1][c]+1)
                    if c<n-1:
                        res[r][c] = min(res[r][c],res[r][c+1]+1)
        
        return res
        
# @lc code=end

