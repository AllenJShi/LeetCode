#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # nums.sort()
        # best = 10000
        # for i in range(len(nums)):
        #     if i>0 and nums[i]==nums[i-1]: continue
        #     left, right = i+1, len(nums)-1
        #     while left < right:
        #         temp = nums[left] + nums[right] + nums[i]
        #         if temp == target: return target
        #         if abs(temp-target) < abs(best-target):
        #             best = temp
        #         if temp > target:
        #             right0 = right-1
        #             while left < right0 and nums[right0]==nums[right]:
        #                 right0 -= 1
        #             right = right0
        #         else:
        #             left0 = left + 1
        #             while left0 < right and nums[left0]==nums[left]:
        #                 left0 += 1
        #             left = left0
        # return best
            
        nums.sort()
        ans = 0
        minDiff = 10000
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                s = nums[left] + nums[right] + nums[i]
                diff = abs(s-target)
                if diff < minDiff:
                    minDiff = diff
                    ans = s
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return ans
        return ans
            
# @lc code=end

