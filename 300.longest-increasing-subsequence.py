#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n)
        dp[0] = 1
        maxL = 1
        for i in range(1,n):
            # i本身就是一个单位的sub
            dp[i] = 1
            # 从0到i-1
            for j in range(0,i):
                # 如果对于每一个i之前的j，存在i大于j的情况
                if nums[i] > nums[j]:
                    # dp更新为当前的dpi或dpj加上一个1中的max
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
# @lc code=end

