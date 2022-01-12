#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        
        def backtracking(depth):
            ans.append(path[:])
            for i in range(depth,len(nums)):
                path.append(nums[i])
                # 注意：此处从i+1进行迭代；在permutation问题中用start/depth+1
                backtracking(i+1)
                path.pop()

        backtracking(0)
        return ans
                
# @lc code=end

