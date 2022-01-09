#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        path = []
        
        def backtracking(sum, startIndex):
            if sum == target:
                # print('path:',type(path))
                # print('path[:]:',type(path[:]))
                ans.append(path[:])
            for i in range(startIndex,len(candidates)):
                if sum+candidates[i] > target:
                    return
                if i > startIndex and candidates[i]==candidates[i-1]:
                    continue
                sum += candidates[i]
                path.append(candidates[i])
                backtracking(sum,i+1)
                sum -= candidates[i]
                path.pop()
        backtracking(0,0)            
        return ans
        
# @lc code=end

