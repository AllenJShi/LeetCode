#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # # dfs solution
        # old2new = {}
        
        # def dfs(node):
        #     if node in old2new:
        #         return old2new[node]

        #     copy = Node(node.val)
        #     old2new[node] = copy
        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfs(nei))
        #     return copy
        
        # return dfs(node) if node else None
    
        # bfs solution
        if not node: return None
        copy = Node(node.val)
        # queue is not being cloned nodes, created but not append neighbors
        cloned, queue = {node:copy}, [node]
        while queue:
            curr = queue.pop()
            for nei in curr.neighbors:
                if nei not in cloned:
                    queue.append(nei)
                    cloned_nei = Node(nei.val)
                    cloned[nei] = cloned_nei
                cloned[curr].neighbors.append(cloned[nei])
        return cloned[node]
        
        
# @lc code=end

