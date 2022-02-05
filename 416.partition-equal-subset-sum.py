#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sanity check 
        if sum(nums) % 2: # or s & 1
            # 若和不为偶数，则不可能存在两个相等的子集
            return False
        
        ############ DP 0/1 knapsack problem ##########
        s = sum(nums)
        # 维护一个s+1的数组
        dp = [True] + [False] * s
        for num in nums:
            # for curr in range(s>>1,num-1,-1): # 此处只考虑s的一半 对应的 return dp[-1]
            for curr in range(s,num-1,-1): #避免下面的curr-num小于0
                # NOTE: 1 <= nums[i] <= 100
                # 之前有curr的和（此时我们不需要多余的num参与进求和），
                # 或，之前在没有num的作用下已形成curr的和（也不需要num参与）
                # 或，curr不能被求得
                dp[curr] = dp[curr] or dp[curr-num]
        # 目标是 一半的和 分别存在两个子集中
        return dp[s//2] # or dp[s >> 1]
        
        
        
        ################ 回溯 （超时）##################
        l , s = len(nums), sum(nums)
        def backtracking(curr, idx):
            if idx == l: # 当到达最后一个idx时，查看当前和是否为一半的总和
                return curr == s>>1
            elif curr + nums[idx] == s>>1 \
                or \
                    (curr + nums[idx] < s<<1 \
                        and backtracking(curr+nums[idx],idx+1)): # select idx and continue to next idx
                return True
            return backtracking(curr, idx+1) # not selecting idx, continue
        return False if s&1 else backtracking(0,0) # s&1若是偶数和则不可能
    
    
        ################## 01背包
        weight = nums
        values = nums
        size = sum(nums) // 2
        if sum(nums) % 2 == 1: return False
        dp = [0] * 10001
        for i in range(len(nums)):
            for j in range(size, nums[i]-1,-1):
                dp[j] = max(dp[j],dp[j-weight[i]]+values[i])
        return size == dp[size]
# @lc code=end

