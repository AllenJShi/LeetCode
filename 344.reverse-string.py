#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        ################ 双指针 #############
        def swap(a,b):
            s[a], s[b] = s[b], s[a]
            
        left = 0
        right = len(s)-1
        while left < right:
            swap(left,right)
            left += 1
            right -= 1
        return s
        
# @lc code=end

