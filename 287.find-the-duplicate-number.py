#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ############## 快慢指针，数组-链表 ###############
        # slow = 0
        # fast = 0
        # slow = nums[slow]
        # fast = nums[nums[fast]]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        # slow = 0
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]
        # return slow
        
        # time O(n) | space O(1)
        
        
        ############## 用下标记录小于等于该下标的元素个数
        n = len(nums)
        left = 0
        right = n-1
        ans = -1
        while left <= right:
            mid = (left + right) / 2
            cnt = 0
            for i in range(n):
                if nums[i] <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        return ans
# @lc code=end

