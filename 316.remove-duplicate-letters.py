#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurance = {}
        visited = set()
        stack = []
        
        for i,char in enumerate(s):
            last_occurance[char] = i
        
        for i, char in enumerate(s):
            if char not in visited:
                while stack and stack[-1]>char and last_occurance[stack[-1]]>i:
                    visited.remove(stack.pop())
                stack.append(char)
                visited.add(char)
                
        return "".join(stack)
    
                
                        
            
                     
                
# @lc code=end

