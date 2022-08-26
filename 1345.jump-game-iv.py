#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#

# @lc code=start
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # # idea:
        # # use BFS to visit neighbors
        # # maitain a dp to record minimum steps to end for each node
        # n = len(arr)
        # if n <= 1: return 0
        
        # queue = [0]
        # visited = [False] * n
        # visited[0] = True
        # dp = [0] * n
        
        # while queue:
        #     u = queue.pop(0)
        #     adjacent = []
        #     if u+1<n and not visited[u+1]: adjacent.append(u+1)
        #     if u-1>=0 and not visited[u-1]: adjacent.append(u-1)
        #     for i in range(u+2,n,1):
        #         if arr[i] == arr[u]:
        #             adjacent.append(i)
        #     print(adjacent)
        #     for v in adjacent:
        #         if not visited[v]:
        #             dp[v] = dp[u]+1
        #             visited[v] = True
        #             queue.append(v)
        # return dp[-1]
        
        
        # 参考答案
        # steps是从任何一点到终点的最短距离，此处初始化为最长的图的距离n-1
        idx_map, steps = defaultdict(list), [len(arr)-1]*len(arr)
        # 值和对应多索引（list）
        for i, num in enumerate(arr):
            idx_map[num].append(i)
        queue = deque([0])
        steps[0] = 0
        while queue:
            idx = queue.popleft()
            if idx == len(arr)-1:
                break
            nxt_step = steps[idx] + 1
            # idx cannot equal to len(arr)-1, because the if condition above
            idx_map[arr[idx]] += [idx+1,idx-1] if idx!=0 else [idx+1]
            while idx_map[arr[idx]]:
                if steps[(other:=idx_map[arr[idx]].pop())] > nxt_step:
                    steps[other] = nxt_step
                    queue.append(other)

        return steps[-1]
        
        
# @lc code=end

