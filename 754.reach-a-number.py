#
# @lc app=leetcode id=754 lang=python3
#
# [754] Reach a Number
#

# @lc code=start
class Solution:
    def reachNumber(self, target: int) -> int:
        numMoves = 0
        def dfs(curr):
            nonlocal numMoves
            if curr==target:
                return numMoves
            numMoves += 1
            return min(dfs(curr+numMoves),dfs(curr-numMoves))
        return dfs(0)
# @lc code=end

