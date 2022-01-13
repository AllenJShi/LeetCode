#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split(' ')
        left = 0
        right = len(arr)-1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
        # NOTE: 'if s' is important!!! 
        arr = [s.strip() for s in arr if s and not s.isspace()]
        
        return ' '.join(arr).strip()
        
# @lc code=end

