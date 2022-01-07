#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # ===================== My Answer =======================
        # if len(nums) == 1: return nums
        
        # isNonIncreasing = True
        # isNonDecreasing = True
        # i = 0
        # while i < len(nums)-1:
        #     if nums[i] > nums[i+1] and isNonIncreasing:
        #         isNonDecreasing = False
                
        #     elif nums[i] < nums[i+1] and isNonDecreasing:
        #         isNonIncreasing = False
                
        #     else:
        #         isNonDecreasing = False
        #         isNonIncreasing = False
        #         break
        #     i += 1
        
        
        # if isNonDecreasing and not isNonIncreasing:
        #     # entire list increasing, swap the last two nums
        #     nums[-1], nums[-2] = nums[-2], nums[-1]
        # elif isNonIncreasing and not isNonDecreasing:
        #     # entire list decreasing, reverse the list
        #     left = 0
        #     right = len(nums)-1
        #     while left < right:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #         right -= 1
        # else:
        #     # swap the last pair increasing nums to decreasing
        #     last, secondlast = len(nums)-1, len(nums)-2
        #     while secondlast >= i:
        #         # if increasing
        #         if nums[secondlast] < nums[last]:
        #             nums[secondlast], nums[last] =\
        #                 nums[last], nums[secondlast]
        #         else:
        #             last = secondlast
        #             secondlast -= 1
        # return nums           
        # ===================== My Answer End ====================
        
        
        i = len(nums) - 2
        
        # backward as decreasing
        # while the latter is less than the former
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1 # start from the last item
            # while the value is less than the one we select
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            # sawp with the least value in the decreasing subarray
            nums[i], nums[j] = nums[j], nums[i]
            
        # reverse the decreasing second half list
        left, right = i+1, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
        return nums
        
        
# @lc code=end

