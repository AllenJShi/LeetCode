#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        def helper(arr):
            if arr[-1] == 9:
                if len(arr) > 1:
                    # NOTE: 加【0】很重要！！！
                    return helper(arr[:-1]) + [0]
                else:
                    arr[-1] = 1
                    arr = arr + [0]
                    return arr
            else:
                arr[-1] += 1
                return arr
            
        return helper(digits)
                
        
# @lc code=end

