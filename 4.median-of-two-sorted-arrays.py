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
        ################### 我的答案 ################
        ######### 直接sorted():
        # m, n = len(nums1), len(nums2)
        # odd = (m+n) % 2
        # nums = sorted(nums1 + nums2)
        # if odd:
        #     median_pos = (m+n) // 2
        #     # go and find the median_pos th element in the sorted combined array
        #     return nums[median_pos]
        # else:
        #     median_left = (m+n) / 2 - 1
        #     median_right = (m+n) / 2 
        #     return (nums[median_left]+nums[median_right]) / 2.0
        
        ######### 思考：
        m, n = len(nums1), len(nums2)
        def getKthElement(k):
            index1, index2 = 0, 0 
            while True:
                if index1 == m:
                    return nums2[index2 + k -1]
                if index2 == n:
                    return nums1[index1 + k -1]
                if k == 1:
                    return min(nums1[index1],nums2[index2])
                newIndex1 = min(index1+k//2-1,m-1)
                newIndex2 = min(index2+k//2-1,n-1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        totalLength = m+n
        if totalLength%2 == 1:
            return getKthElement((totalLength+1)//2)
        else:
            return (getKthElement(totalLength//2)+getKthElement(totalLength//2+1))/2.0
        
            
        
# @lc code=end

