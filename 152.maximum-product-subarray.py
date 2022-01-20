#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#

# @lc code=start

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxP, minP, ans = nums[0], nums[0], nums[0]
        for i in range(1,n):
            curMax, curMin, = maxP, minP 
            maxP = max(curMax * nums[i], nums[i], curMin * nums[i])
            minP = min(curMin * nums[i], nums[i], curMax * nums[i])
            ans = max(maxP, ans)
        return ans
# @lc code=end

