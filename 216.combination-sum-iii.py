#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#

# @lc code=start
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        if not k*n:
            return []

        def backtracking(idxStart,sum):
            # if len(path) == k:
            #     if sum(path[:]) == n:
            #         ans.append(path[:])
            #     return
            if sum>n:
                return
            if sum==n and len(path)==k:
                return ans.append(path[:])
            
            # 用sum减少每一次求和的时间，没有太大作用
            for i in range(idxStart,9-(k-len(path))+2):
                path.append(i)
                sum += i
                backtracking(i+1,sum)
                path.pop()
                sum -= i
                
        backtracking(1,0)
        return ans
        
# @lc code=end

