#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        ############# recursive #############
        ###### naive solution (TLE)
        # def dfs(index: int) -> int:
        #     if index < 0:
        #         return 0
        #     return max(dfs(index-2)+nums[index],dfs(index-1))
        # return dfs(len(nums)-1)
        ###### memo 
        # memo = [-1] * len(nums)
        # def dfs(index: int) -> int:
        #     nonlocal memo
        #     if index < 0:
        #         return 0
        #     if memo[index] >= 0:
        #         return memo[index]
        #     res = max(dfs(index-2)+nums[index],dfs(index-1))
        #     memo[index] = res
        #     return res
        # return dfs(len(nums)-1)
        
        
        ############ iterative ###########
        ##### naive dp solution
        # if not len(nums): return 0
        # dp = [-1] * (len(nums)+1)
        # dp[0] = 0
        # dp[1] = nums[0]
        # for i in range(1,len(nums)):
        #     dp[i+1] = max(dp[i],dp[i-1]+nums[i])
        # return dp[-1]
        
        ##### memory efficient solution
        # idea: only need to remember i-1 and i for i+1
        if not len(nums): return 0
        prev, curr = 0, nums[0]
        for i in range(1,len(nums)):
            tmp = max(curr,prev+nums[i])
            prev, curr = curr, tmp
        return curr

            
# @lc code=end

