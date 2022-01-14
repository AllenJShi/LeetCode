#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start
from bisect import bisect


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ################# 模拟 #######################
        # if n==1:
        #     return True
        # s = set()
        # s.add(n)
        # def helper(n):
        #     string = str(n)
        #     sum = 0
        #     for i in string:
        #         sum += int(i)**2
        #     if sum in s:
        #         return False
        #     else:
        #         s.add(sum)
        #     if sum == 1:
        #         return True
        #     else:
        #         return helper(sum)
        
        # return helper(n)
        
        ################# 快慢指针 #################
        def bitSquareSum(n):
            sum = 0
            while n>0:
                bit = n % 10
                sum += bit**2
                n= n /10
            return sum
        
        # slow, fast = n, n
        # while True:
        #     slow = bitSquareSum(slow)
        #     fast = bitSquareSum(fast)
        #     fast = bitSquareSum(fast)
        #     if slow == fast:
        #         break
        # return slow==1
        
        slow, fast = n, bitSquareSum(n)
        while fast!=1 and slow!=fast:
            slow = bitSquareSum(slow)
            fast = bitSquareSum(bitSquareSum(fast))
        return fast==1
# @lc code=end

