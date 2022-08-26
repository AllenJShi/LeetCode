#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start

class UnionFind:
    def __init__(self,n) -> None:
        self.rank = [1]*n
        self.parent = [i for i in range(n)]
        
    def find(self,x):
        # if self.parent[x]!=x:
        #     self.parent[x] = self.find(x)
        # return self.parent[x]
        while self.parent[x]!=x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self,x,y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return 0
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
            self.rank[y_root] += 1
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        return 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        edges = []
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    edges.append([i,j])
        print(edges)
        uf = UnionFind(n)
        res = n
        for u,v in edges:
            res -= uf.union(u,v)
        return res
# @lc code=end

