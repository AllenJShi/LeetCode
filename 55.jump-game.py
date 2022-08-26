#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy solution
        # from the end, backward shifting the right edge
        goal = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                # shrink the right boundry to the current position
                goal = i
        return goal == 0
    
                
                
# @lc code=end

