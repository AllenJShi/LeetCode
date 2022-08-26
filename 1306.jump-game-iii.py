#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # BFS solution
        # go to each reachable (adjacent) node
        # if the adjacent node with value 0, return true
        # else keep traversing the graph
        visited = [False] * len(arr)
        visited[start] = True
        queue = [start]
        while queue:
            u = queue.pop(0) # pop the leftmost one
            val = arr[u]
            # the next line is the only variation, where we define the problem
            if val == 0: return True
            if 0 <= u < len(arr):
                for i in [val,-val]: # the only two adjacent nodes possible
                    v = u + i
                    if 0<=v<len(arr) and not visited[v]:
                        queue.append(v)
                        visited[v] = True
        return False
                    
# @lc code=end

