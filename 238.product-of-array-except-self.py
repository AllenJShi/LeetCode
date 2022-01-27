#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ############### 左右双数组 #############
        # n = len(nums)
        # L = [1] * n
        # R = [1] * n
        # ans = [1] * n
        # for i in range(1,n):
        #     L[i] = L[i-1] * nums[i-1]
        #     R[n-i-1] = R[n-i] * nums[n-i]
        # # for j in range(n-1-1,0-1,-1):
        # #     R[j] = R[j+1] * nums[j+1]
        # for k in range(n):
        #     ans[k] = L[k] * R[k]
        # return ans
        
        # time O(n) | space O(n)
        
        
        ######### 空间优化 ###########
        n = len(nums)
        ans = [1] * n
        left = 1
        right = 1
        for i in range(n-1):
            left *= nums[i]
            ans[i+1] = left
        for j in range(n-1, 0, -1):
            right *= nums[j]
            ans[j-1] *= right
        return ans
    
        #  time O(n) | space O(1)
        
# @lc code=end

