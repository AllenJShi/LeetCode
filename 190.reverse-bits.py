#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bitsize = 32
        
        ############ 变成string后，反转 #####################
        # binary = bin(n)
        # reverse = binary[-1:1:-1]
        # reverse = reverse + (bitsize-len(reverse))*'0'
        # return int(reverse,2)
        
        ############## bitwise manipulation ##############
        res = 0
        for _ in range(bitsize):
            res = (res<<1)|(n&1)
            n >>= 1
        return res
        

# @lc code=end

