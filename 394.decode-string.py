#
# @lc app=leetcode id=394 lang=python
#
# [394] Decode String
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ################ 递归 ################
        # def backtracking(i):
        #     res, multi = "", 0
        #     while i < len(s):
        #         if '0' <= s[i] <= '9':
        #             multi = multi * 10 + int(s[i])
        #         elif s[i] == '[':
        #             i, tmp = backtracking(i+1)
        #             res += tmp * multi
        #             multi = 0
        #         elif s[i] == ']':
        #             return i, res
        #         else:
        #             res += s[i]
        #         i += 1
        #     return res
        # return backtracking(0)
        
        ############## 迭代 ###############
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi,res])
                res, multi = "",0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res
# @lc code=end


