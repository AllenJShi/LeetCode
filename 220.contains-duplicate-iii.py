#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # # sliding window (TLE)
        # left = 0
        # while left < len(nums):
        #     for i in range(1,k+1):
        #         if left+i < len(nums) and abs(nums[left]-nums[left+i]) <= t:
        #             return True            
        #     left += 1
        # return False
    
    
        # ordered map
        sorted_idx = sorted(range(len(nums)),key=lambda x:nums[x])
        sorted_nums = [nums[idx] for idx in sorted_idx]
        
        # binary search
        l,r = 0, 1 # two points on the ordered list
        while r < len(nums):
            if sorted_nums[r] - sorted_nums[l] <= t:
                if abs(sorted_idx[l]-sorted_idx[r]) <= k:
                    return True
                r += 1 # select a larger right so right-left still valid but may have idx work
            else:
                l += 1 # select a larger left so right-left<=t
                r = l + 1
        return False
            
        
        
# @lc code=end

