#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ################# 我的答案（passed很慢）###############
        # temp = ''
        # for i in range(len(s)):
        #     if s[i].isnumeric() or s[i].isalpha():
        #         temp += s[i].lower()

        # left,right = 0, len(temp)-1
        # while left < right:
        #     if temp[left] != temp[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True
        
        ################### 参考 ##################
        # sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        # n = len(sgood)
        # left,right = 0, n-1
        # while left < right:
        #     if sgood[left] != sgood[right]:
        #         return False
        #     left, right = left+1, right-1
        # return True    
        
        
        ################# 直接操作 ###############
        n = len(s)
        left, right = 0, n-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower()!=s[right].lower():
                    return False
                left, right = left+1, right-1
        return True
        # Memory O(1) | Time O(n)


# @lc code=end

