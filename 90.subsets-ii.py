#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        path = []
        nums.sort()
        
        def backtracking(depth):
            ans.append(path[:])
            for i in range(depth,len(nums)):
                if i>depth and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                # 注意：此处从i+1进行迭代；在permutation问题中用start/depth+1
                backtracking(i+1)
                path.pop()

        backtracking(0)
        return ans
        
# @lc code=end

