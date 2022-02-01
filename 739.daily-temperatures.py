#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ############# （超时答案）
        # n = len(temperatures)
        # ans = [0] * n
        
        # def waitUntil(start, target):
        #     for i in range(start,n):
        #         if temperatures[i] > target:
        #             return i - start + 1
        #     return 0
        
        # for i in range(n):
        #     ans[i] = waitUntil(i+1,temperatures[i])
        # return ans
        
        
        ############# iterative （超时答案）
        # n = len(temperatures)
        # ans = [0] * n
        # for i in range(n):
        #     curr_tmp = temperatures[i]
        #     for j in range(i+1,n):
        #         if temperatures[j] > curr_tmp:
        #             ans[i] = j - i
        #             break     
        # return ans


        ########### 参考答案 #################
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                t = stack.pop()
                ans[t] = i - t
            stack.append(i)
        return ans
# @lc code=end

