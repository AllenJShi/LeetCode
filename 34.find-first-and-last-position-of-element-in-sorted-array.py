#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(log n) implement binary search



        # ==================== My Answer =====================
        # def helper(nums, target, left, right):
        #     if right > left:
        #         mid = left + (right - left) // 2
        #         if nums[mid] == target:
        #             return mid
        #         elif nums[mid] > target:
        #             return helper(nums, target, left, mid-1)
        #         else:
        #             return helper(nums,target, mid+1, right)
        #     else:
        #         return -1
        
        
        # pos = helper(nums,target,0,len(nums)-1)

        # if pos>=0:
        #     i = pos-1
        #     j = pos+1
            
        #     while i>0 and nums[i] == target:
        #         i -= 1
        #     while j<len(nums)-1 and nums[j] == target:
        #         j += 1
            
        #     return [i+1,j-1]
        
        # return [-1,-1]
        # ====================================================
        
        
        def helper(nums, target):
            left = 0
            right = len(nums) - 1
            ans = len(nums)
            while left <= right:
                mid = (left + right)//2
                if nums[mid] >= target:
                    right = mid - 1
                    ans = mid
                else:
                    left = mid + 1
            return ans
        
        left = helper(nums,target-1)
        right = helper(nums,target) -1
        if left<=right and nums[left] == target:
            return [left,right]
        return [-1,-1]
        
# @lc code=end

