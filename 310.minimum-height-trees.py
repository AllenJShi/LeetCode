#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edgeset = [set() for _ in range(n)]
        for u,v in edges:
            edgeset[u].add(v)
            edgeset[v].add(u)
        queue = [x for x in range(n) if len(edgeset[x])<2]
        tmp = []
        while True:
            for node in queue:
                for nei in edgeset[node]:
                    edgeset[nei].remove(node)
                    if len(edgeset[nei]) == 1:
                        tmp.append(nei)
            if not tmp:
                break
            tmp, queue = [], tmp
        return queue
# @lc code=end

