#
# @lc app=leetcode id=179 lang=python
#
# [179] Largest Number
#

# @lc code=start
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
        #             nums[i], nums[j] = nums[j] , nums[i]
                            
        # return "".join(map(str,nums)) if nums[0] != 0 else "0"
    
    
        ############### 参考答案 #######################
        nums_str = map(str, nums)
        compare = lambda x, y: 1 if x+y < y+x else -1
        nums_str.sort(cmp=compare)
        return "0" if nums_str[0] == "0" else "".join(nums_str)
        
        
        
# @lc code=end

