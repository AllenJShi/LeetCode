#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ############### 排序 ##################
        # nums.sort()
        # for i in range(len(nums)):
        #     if i!=nums[i]:
        #         return i
        # return len(nums)
    
        # # time O(nlogn) | memory O(logn)
        
        
        ############### 哈希 ##################
        # s = set(nums)
        # for i in range(len(nums)+1):
        #     if i not in n:
        #         return i
        # # time O(n) | memory O(n)
        
        ############## 位运算 ###############
        # xor = 0
        # for i, num in enumerate(nums):
        #     xor ^= i^num
        # return xor^len(nums)
        # # time O(n) | memory O(1)

        ################ 数学求和 ###############
        n = len(nums)
        total  = n*(n+1)//2
        return total - sum(nums)       
        # time O(n) | space O(1)
        
# @lc code=end

