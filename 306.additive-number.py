#
# @lc app=leetcode id=306 lang=python
#
# [306] Additive Number
#

# @lc code=start
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def backtracking(prev, curr,num):
            # 1.num中不足3个数字
            if len(num) < 3: return False
            # 2.排除0开头的问题，当0排在开头时，str和int是不同的
            p, c = int(num[:prev]), int(num[prev:prev+curr])
            if str(p) != num[:prev] or str(c) != num[prev:prev+curr]:
                return False
            # 3.subarray的长度-prev-curr小于第一个或第二个数字的长度
            # 则，求和后一定比第三个数字大
            if len(num) - prev - curr < max(prev, curr):
                return False
            # 下一个数字预期与求和相同
            nxt = str(p+c)
            x = len(nxt)
            if num[prev+curr:prev+curr+x] != nxt:
                return False
            if num[prev+curr:]==nxt: return True
            return backtracking(curr,x,num[prev:])
        
        n = len(num)
        for i in range(1,n):
            for j in range(1,n-i):
                if backtracking(i,j,num):
                    return True
        return False
# @lc code=end

