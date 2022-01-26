#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        odd = (m+n) % 2
        p1,p2 = 0, 0
        ans = 0
        nums = sorted(nums1 + nums2)
        if odd:
            median_pos = (m+n) // 2
            # go and find the median_pos th element in the sorted combined array
            
            return nums[median_pos]
        else:
            median_left = (m+n) / 2 -1
            median_right = (m+n) / 2 
            return (nums[median_left]+nums[median_right]) / 2.0
# @lc code=end

