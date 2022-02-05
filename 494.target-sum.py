#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # NOTE: nonlocal只能用在python3
        
        # ############ 超时
        # def backtracking(i,s):
        #     nonlocal cnt
        #     if i==n:
        #         if s == target:
        #             cnt += 1
        #     else:
        #         backtracking(i+1,s+nums[i])
        #         backtracking(i+1,s-nums[i])
        # cnt = 0
        # n = len(nums)
        # backtracking(0,0)
        # return cnt
        
        # time O(2^n) | space O(n)
        
        ############ 优化超时 + 记忆
        cache = {}
        def dfs(u, curr):
            key = str(u) + "_" + str(curr)
            # NOTE: fstring只能在python3中使用
            # key = f'{u}_{curr}'
            if key in cache:
                return cache[key]
            if u==len(nums):
                cache[key] = 1 if curr==target else 0
                return cache[key]
            left = dfs(u+1, curr+nums[u])
            right = dfs(u+1, curr-nums[u])
            cache[key] = left + right
            return cache[key]
        return dfs(0,0)
    
    
        ############ DP ##############
        n = len(nums)
        s = 0
        for num in nums:
            s += abs(num)
        if abs(target) > s: return 0
        dp = [[0] * (2*s+1) for _ in range(n+1)]
        dp[0][0 + s] = 1
        for i in range(1,n+1):
            x = nums[i-1]
            for j in range(-s,s+1,1):
                if j-x+s >= 0:
                    dp[i][j+s] += dp[i-1][j-x+s]
                if j+x+s <= 2*s:
                    dp[i][j+s] += dp[i-1][j+x+s]
        return dp[n][target+s]
        
# @lc code=end

