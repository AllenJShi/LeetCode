#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 遍历，碰到0就删除，在最后再加上相同个数的0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                # del nums[i]
                nums.pop(i)
                count += 1
                i -= 1
        return nums + [0]*count
# @lc code=end

