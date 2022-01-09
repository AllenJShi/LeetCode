#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        combo = []
        if len(candidates)==0:
            return []
        
        def dfs(target, combo, idx):
            if idx == len(candidates):
                return
            
            if target == 0:
                ans.append(combo)
                return
            
            for i in range(idx, len(candidates)):
                residual = target - candidates[i]
                if residual < 0:
                    return
                dfs(residual,combo+[candidates[i]],i)
                            
        dfs(target,combo,0)
        return ans
# @lc code=end

