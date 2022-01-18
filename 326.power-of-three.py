#
# @lc app=leetcode id=326 lang=python
#
# [326] Power of Three
#

# @lc code=start
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ################### 我的答案 passed ################
        # # brute force
        # if n==1:
        #     return True
        # ans = 1
        # while ans < n:
        #     ans *= 3
        #     if ans == n:
        #         return True
        #     if ans > n:
        #         return False
        
        ################ 参考答案 ##################
        # # 测试除以3
        # while n and n % 3==0:
        #     n /= 3
        # return n==1

        # # 是不是32位最大的3的约数
        return n>0 and 3**19 % n == 0 
        
        
# @lc code=end

