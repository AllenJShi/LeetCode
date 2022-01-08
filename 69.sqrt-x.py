#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ############### My answer (passed) ###############
        # if x==0:
        #     return 0
        # ans = 1
        # while ans < x:
        #     if (ans*ans == x) or (ans*ans < x < (ans+1)*(ans+1)):
        #         return ans
        #     ans += 1
        # return ans
        
        ############## Binary Search #################
        left, right, ans = 0, x, -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
        
        
# @lc code=end

