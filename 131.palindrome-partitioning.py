#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []       
        path = [] 
        
        def backtracking(idxStart):
            if idxStart >= len(s):
                return ans.append(path[:])
            
            for i in range(idxStart, len(s)):
                if isPalindrome(idxStart,i):
                    path.append(s[idxStart:i+1])
                else:
                    continue
                backtracking(i+1)
                path.pop()
                
        def isPalindrome(start,end):
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True
        
            # substring = s[start:end+1]
            # if substring==substring[::-1]:
            #     return True
            # else:
            #     return False
        
        backtracking(0)
        return ans
        
        
# @lc code=end

