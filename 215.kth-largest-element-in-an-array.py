#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums.sort()
        # return nums[-k]
        
        
        ######## quick sort ###########
        def swap(left, right):
            nums[left], nums[right] = nums[right], nums[left]
            
            
        def quickSelect(start,end):
            n = len(nums)
            left, right = start, end
            pivot = left
            
            while left < right:
                while left <  right and nums[right] >= nums[pivot]:
                    right -= 1
                while left < right and nums[left] <= nums[pivot]:
                    left += 1
                swap(left, right)
            swap(pivot,right)
            
            if right == n-k:
                return nums[right]
            elif right < n-k:
                return quickSelect(right+1,end)
            else:
                return quickSelect(start, right-1)
        return quickSelect(0,len(nums)-1)
    
    # time O(n) | space O(1)
    
    
    
# @lc code=end

