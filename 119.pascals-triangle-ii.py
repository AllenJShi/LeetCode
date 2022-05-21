#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1 for _ in range(rowIndex+1)]
        for i in range(rowIndex):
            for j in range(i,0,-1):
                res[j] = res[j] + res[j-1]
                print(res)
        return res
# @lc code=end

