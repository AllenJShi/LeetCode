#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        operations = {
            '+':add,
            '-':sub,
            '*':mul,
            '/':lambda x,y:int(x/float(y)),
        }
        
        stack = []
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = operations[token](num1,num2)
            finally:
                stack.append(num)
        return stack[0]
        
        # n = len(tokens)
        # stack = [0]*((n+1)//2)
        # index = -1
        # for token in tokens:
        #     try:
        #         num = int(token)
        #         index += 1
        #         stack[index] = num
        #     except:
        #         index -= 1
        #         stack[index] = operations[token] (stack[index],stack[index+1])
        # return stack[0]
        
        
        
        # time O(n) | space O(n)
# @lc code=end

