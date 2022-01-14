#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        ################ 模拟 time O(n), memory O(n) ###################
        # s = set()
        # while nums:
        #     num = nums.pop()
        #     if num not in s:
        #         s.add(num)
        #     else:
        #         return True
        # return False

        ############### 排序 time O(nlogn), memory O(logn) ###################
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    

        
# @lc code=end

