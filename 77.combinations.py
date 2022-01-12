#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        
        if not n*k:
            return []
        
        def backtracking(idx):
            if len(path)==k:
                ans.append(path[:])
                return
            # n-(k-path size)+2 进行剪枝
            # 后面的元素已经在前面的path中被考虑
            # 这里我们不考虑permutation order
            # 所以可以剔除之后的组合方式
            for i in range(idx,n-(k-len(path))+2):
                path.append(i)
                # 注意：要从下一个位置开始
                backtracking(i+1)
                path.pop()
                
        backtracking(1)
        return ans
        
# @lc code=end

