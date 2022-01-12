#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        ans = []
        path = []
        
        keyboard = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        
        def backtracking(idx):
            if idx == len(digits):
                ans.append("".join(path))
                return
            digit = ord(digits[idx]) - ord('0')
            for letter in keyboard[digit]:
                path.append(letter)
                backtracking(idx+1)
                path.pop()
        backtracking(0)
        return ans
                
        
# @lc code=end

