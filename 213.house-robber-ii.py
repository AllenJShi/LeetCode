#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        ########## recursive ##########
        ###### memo solution 
        # idea: the first and last cannot be robbed on the same night
        # this leads to exclude either one from nums, then run the same algorithm as lc198
        # memo = [-1] * (len(nums)+1)
        # def dfs(nums: List[int], index: int) -> int:
        #     if index < 0:
        #         return 0
        #     if memo[index] > 0:
        #         return memo[index]
        #     res = max(dfs(nums,index-1),dfs(nums,index-2)+nums[index])
        #     memo[index] = res
        #     return res
        # return max(dfs(nums[1:],len(nums)-2),dfs(nums[:-1],len(nums)-2))
    
    
        ########### iterative #############
        if not len(nums):return 0
        if len(nums)==1:return nums[0]
        def helper(nums):
            rob_, not_rob_ = 0, 0
            for num in nums:
                rob_, not_rob_ = not_rob_+num, max(rob_,not_rob_)
            return max(rob_,not_rob_)
        return max(helper(nums[1:]),helper(nums[:-1]))    

        
# @lc code=end

