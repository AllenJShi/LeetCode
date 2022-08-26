#
# @lc app=leetcode id=1340 lang=python3
#
# [1340] Jump Game V
#

# @lc code=start
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        # # problem statement:
        # # max number of indices is equivalent to the longest path in each graph
        # # NOTE: this is a directed graph
        # # idea:
        # # 1. run dfs on each graph (starting at each possible index)
        # # 2. use seen to track max length from each root(starting) node

        # seen = dict()
        
        # def dfs(node):
        #     if node in seen:
        #         return

        #     seen[node] = 1
            
        #     # to the left of the pivot node
        #     i = node - 1
        #     while i >= 0 and node-i <= d and arr[node] > arr[i]:
        #         dfs(i)
        #         seen[node] = max(seen[node],seen[i]+1)
        #         i -= 1   # look to the left side in order
            
        #     # to the right of the pivot node
        #     i = node + 1
        #     while i < len(arr) and i-node <= d and arr[node] > arr[i]:
        #         dfs(i)
        #         seen[node] = max(seen[node],seen[i]+1)
        #         i += 1
        
        # # dfs on each index as root
        # for root in range(len(arr)):
        #     dfs(root)
            
        # return max(seen.values())
    
    
    
        # alternative solution: DP
        dp = [1] * len(arr)
        L = [(arr[i],i) for i in range(len(arr))]
        # sort based on height, so in the for loop always start from the lowest bar
        L = sorted(L,key=lambda x:x[0])
        # from the lower bar to higher, this guarantees all lower (contraints) are calculated before higher
        # so the dp is accurate
        for h, i in L:
            cur = 1
            # look to the left side
            for idx in range(i-1,max(0,i-d)-1,-1):
                if arr[idx] >= h:
                    break
                cur = max(dp[idx]+1,cur)
            # look to the right side
            for idx in range(i+1, min(len(arr),i+d+1)):
                if arr[idx] >= h:
                    break
                cur = max(dp[idx]+1,cur)
            dp[i] = cur
        return max(dp)
    
# @lc code=end

