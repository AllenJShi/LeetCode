#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ######## 我的答案 （一次通过！！！）#########
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
        return right
        
        # time O(logn) | space O(1)
        
        ############ 参考答案 ################
        ####### 二分查找：time O(logn) | space O(1)
        # n = len(nums)

        # def get(i):
        #     if i==-1 or i==n:
        #         return float('-inf')
        #     return nums[i]
        
        # left, right, ans = 0, n-1, -1
        # while left <= right:
        #     mid = (left+right) // 2
        #     if get(mid-1) < get(mid) > get(mid+1):
        #         ans = mid
        #         break
        #     if get(mid) < get(mid+1):
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return ans
            
            
        ############ 迭代: time O(n) | space O(1)
        # n = len(nums)
        # idx = random.randint(0,n-1)
        # def get(i):
        #     if i==-1 or i==n:
        #         return float('-inf')
        #     return nums[i]

        # while not (get(idx-1) < get(idx) > get(idx+1)):
        #     if get(idx) < get(idx+1):
        #         idx += 1
        #     else:
        #         idx -= 1
        # return idx
        
# @lc code=end

