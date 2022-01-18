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
        ############## 我的答案 passed ###############
        # # 遍历，碰到0就删除，在最后再加上相同个数的0
        # count = 0
        # i = 0
        # while True:
        #     if i >= len(nums):
        #         break
        #     if nums[i] == 0:
        #         # del nums[i]
        #         nums.pop(i)
        #         count += 1
        #         i -= 1
        #     i += 1
        # nums += [0] * count
        
        ############### 参考答案 ##############
        ################ 双指针 ##############
        n = len(nums)
        left, right = 0, 0
        while right < n:
            # 若右指针不为0，则与后一个互换
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            # 若右指针为0，则往后寻找第一个0
            right += 1
        
# @lc code=end

