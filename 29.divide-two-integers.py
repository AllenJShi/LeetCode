#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # quick check if trivial case
        if dividend == 0: return 0
        # determine the sign first
        is_negative = (dividend > 0 > divisor) or (divisor > 0 > dividend)
        # take the absolute
        dividend, divisor = abs(dividend), abs(divisor)
        # quick check if trivial case
        if dividend == divisor:
            return -1 if is_negative else 1
        # init a counter of the number of divisor 
        quotient = 0
        # update the dividend (decrease in value)
        while divisor <= dividend:
            # the_sum is value of a number of divisor containing in dividend
            the_sum = divisor
            # the number of divisor (in value, the_sum)
            num_quotients_added = 1
            # while until there is no more room for additional divisor
            while the_sum + the_sum <= dividend:
                # double the value
                the_sum += the_sum
                # double the number, ie 2 divisors -> 4 divisors
                num_quotients_added += num_quotients_added
            # decrease the value of current dividend
            dividend -= the_sum
            # store the current number of quotients
            quotient += num_quotients_added
        if is_negative:
            return -min(quotient, 2e31)
        else:
            return min(quotient,2**31-1)
            
        
# @lc code=end

