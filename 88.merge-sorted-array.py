#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        tail = m+n-1
        while m-1>=0 or n-1>=0:
            if m == 0:
                nums1[tail] = nums2[n-1]
                n -= 1
            elif n == 0:
                nums1[tail] = nums1[m-1]
                m -= 1
            elif nums1[m-1] < nums2[n-1]:
                nums1[tail] = nums2[n-1]
                n -= 1
            else:
                nums1[tail] = nums1[m-1]
                m -= 1       
            tail -= 1
# @lc code=end

