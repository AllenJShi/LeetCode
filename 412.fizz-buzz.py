#
# @lc app=leetcode id=412 lang=python
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = [""]*n
        
        for i in range(n):
            div = i+1
            if div%3==0 or div%5==0:
                if div%3==0:
                    ans[i] += "Fizz"
                if div%5==0:
                    ans[i] += "Buzz"
            else:
                ans[i] += str(div) 

        return ans
        
        
        
# @lc code=end

