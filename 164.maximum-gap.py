#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        nums.sort()
        res = 0
        for i in range(1,len(nums)):
            res = max(res,nums[i]-nums[i-1])
        return res
# @lc code=end

