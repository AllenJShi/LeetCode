#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        left, right = 0, 0 # window edge pointers
        # 1D BFS
        # only the sliding window moving
        while right < len(nums) - 1:
            # while the right edge is not reach the end
            farthest = 0 # keep track of the farthest position reachable
            for i in range(left, right + 1):
                farthest = max(farthest, i+nums[i])
            left = right + 1 # move the window to the right
            right = farthest
            res += 1 # increment steps
            
        return res

# @lc code=end