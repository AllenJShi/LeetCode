#
# @lc app=leetcode id=532 lang=python
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(nums)
        ans = 0
        nums.sort()
        
        # track all unique pairs
        paired = []
        
        for i in range(n):
            if i-1 >= 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1,n):
                diff = nums[j] - nums[i]
                if diff == k and (nums[i],nums[j]) not in paired:
                    ans += 1
                    paired.append((nums[i],nums[j]))
                elif diff > k:
                    break
        return ans
        
# @lc code=end

