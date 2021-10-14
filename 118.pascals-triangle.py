#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            currlayer = []
            for j in range(0,i+1):
                if j == 0 or j == i:
                    currlayer.append(1)
                else:
                    currlayer.append(ans[i-1][j]+ans[i-1][j-1])
            ans.append(currlayer)
        return ans
        
# @lc code=end

