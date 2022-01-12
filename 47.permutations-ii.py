#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        visited = [False] * len(nums)
        nums.sort()      
        
        def backtracking(start):
            if start == len(nums):
                return ans.append(path[:])
            
            for i in range(len(nums)):
                # not visited i-1 is crucial
                # this assures i-1 is not in the current path
                # and thus unique
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    backtracking(start+1)
                    path.pop()
                    visited[i] = False
                
        backtracking(0)
        return ans
        
        
        
# @lc code=end

