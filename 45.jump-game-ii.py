#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ############# DP 我的答案 ##############
        # n = len(nums)
        # dp = [float('inf')] * n
        # dp[0] = 0
        
        # for i in range(n):
        #     maxStride = nums[i]
        #     while maxStride > 0:
        #         if i+maxStride < n:
        #             dp[i+maxStride] = min(dp[i+maxStride],dp[i]+1)            
        #         maxStride -= 1
        # return dp[-1]
    
    
        ########### 参考答案 #################
        ########### 反向查找 -- 贪心算法
        # position = len(nums) - 1
        # steps = 0
        # while position > 0:
        #     for i in range(position):
        #         if i+nums[i] >= position:
        #             position = i
        #             steps += 1
        #             break
        # return steps
    
        # time O(n^2) | space O(1)
        
        ########## 正向查找
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n-1):
            if maxPos >= i:
                maxPos = max(maxPos, i+nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
        # time O(n) | space O(1)
    
# @lc code=end

