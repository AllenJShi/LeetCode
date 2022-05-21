#
# @lc app=leetcode id=227 lang=python
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ########## 我的答案 108/109 最后一个case超时 ################
        # n = len(s)
        # idx = 0
        # stack = []
        # prev = ''
        # while idx < n:
        #     if '0' <= s[idx] <= '9':
        #         prev += s[idx]
        #     else: # operators or space
        #         if prev!='':
        #             stack.append(int(prev))
        #             prev = ''
        #         if s[idx] in ['+','-']:
        #             stack.append(s[idx])
        #         elif s[idx] in ['*','/']:
        #             j = idx + 1
        #             post = ''
        #             while j < n and ('0' <= s[j] <= '9' or s[j]==' '):
        #                 post += s[j]
        #                 j += 1
        #             numerator = stack.pop()
        #             stack.append(int(numerator * int(post)) if s[idx]=='*' else int(numerator / int(post)))
        #             idx = j - 1
        #         else: # space
        #             while idx < n and s[idx] == ' ':
        #                 idx += 1
        #             idx -= 1
        #     idx += 1
        # if prev:
        #     stack.append(int(prev))
        # while len(stack) > 1:
        #     first = stack.pop(0)
        #     operator = stack.pop(0)
        #     second = stack.pop(0)
        #     stack.insert(0,first + second if operator=='+' else first - second)
        # return stack[-1]
            
        ################################
        n = len(s)
        if n==0: return 0
        stack = []
        curr = 0
        operation = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                curr = curr * 10 + int(char)
            if (not char.isdigit() and char != ' ') or i==n-1:
                if operation == '-':
                    stack.append(-curr)
                elif operation == '+':
                    stack.append(curr)
                elif operation == '*':
                    last = stack.pop()
                    stack.append(last * curr)
                elif operation == '/':
                    last = stack.pop()
                    stack.append(last//curr if last*curr>0 else (last+(-last%curr))//curr)
                operation = char
                curr = 0
        result = 0
        while stack:
            result += stack.pop()
        return result            
        
            
        ############### 参考答案 ###############
        last, curr, result, prev = 0, 0, 0, '+'
        for i, char in enumerate(s):
            if char.isdigit():
                curr = 10 * curr + int(char)
            if char in ('+','-','*','/') or i == len(s) - 1:
                if prev == '+':
                    result += last
                    last = curr
                elif prev == '-':
                    result += last
                    last = -curr
                elif prev == '*':
                    last = last * curr
                elif prev == '/':
                    last = last//curr if last*curr>0 else (last+(-last%curr))//curr
                prev = char
                curr = 0
        result += last
        return result
    
# @lc code=end

