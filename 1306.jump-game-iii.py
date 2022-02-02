#
# @lc app=leetcode id=1306 lang=python
#
# [1306] Jump Game III
#

# @lc code=start
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        ################## 我的答案 ###############
        # def backtracking(next_position):   
        #     if next_position >= n or next_position < 0 or visited[next_position]:
        #         return False
        #     if arr[next_position] == 0:
        #         return True
        #     visited[next_position] = True
        #     return backtracking(next_position + arr[next_position]) \
        #         or backtracking(next_position - arr[next_position])
        # n = len(arr)
        # # 用visited进行剪枝，非常重要！！！否则无法通过时间
        # visited = [False] * n
        # return backtracking(start)
    
        ################## BFS ######################
        # n = len(arr)
        # visited  = [False] * n
        
        # if arr[start] == 0: return True
        
        # queue = [start]
        # visited[start] = True
        # while queue:
        #     node = queue.pop(0)
        #     if node + arr[node] < n and not visited[node + arr[node]]:
        #         if (arr[node + arr[node]] == 0):
        #             return True
        #         queue.append(node + arr[node])
        #         visited[node + arr[node]] = True
        #     if node - arr[node] >= 0 and not visited[node - arr[node]]:
        #         if (arr[node - arr[node]] == 0):
        #             return True
        #         queue.append(node - arr[node])
        #         visited[node - arr[node]] = True
        # return False


        ############## 优化参考答案 #################
        if arr[start] == 0:
            return True

        n = len(arr)
        used = {start}
        q = collections.deque([start])

        while len(q) > 0:
            u = q.popleft()
            for v in [u + arr[u], u - arr[u]]:
                if 0 <= v < n and v not in used:
                    if arr[v] == 0:
                        return True
                    q.append(v)
                    used.add(v)
        
        return False

# @lc code=end

