#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ############# binary search ##############
        if num <= 1: return True
        left, right = 0, num
        while left <= right:
            mid = (left+right)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                right = mid-1
            else:
                left = mid+1
        return False
        
        
        ############ newton's method ##############
        mid = num
        while mid**2 > num:
            # need to consider the odd numbers
            mid  = (mid + num//mid) // 2
        return mid**2 == num
# @lc code=end

