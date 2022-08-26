#
# @lc app=leetcode id=1696 lang=python3
#
# [1696] Jump Game VI
#

# @lc code=start
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """
        # 思路1：失败
        # choose the greater valued index
        # greedy idea:
        # because you can go 0 to k, which is continuous
        # so everytime just pick the max valued position
        # and it guarantees that there is no such case where 
        # you must pick a smaller to obtain an eventually larger
        # due to the continuity
        # it also guarantees to reach the end
        n = len(nums)
        start = 0
        dp = [0] * n
        dp[start] = nums[start]
        while start + 1 < n:
            idxmax = start + 1
            curr_val = nums[idxmax]
            for i in range(idxmax+1,start+k+1,1):
                if i<n and curr_val < nums[i]:
                    curr_val = nums[i]
                    idxmax = i
            dp[idxmax] = curr_val + dp[start]
            start = idxmax
        return dp[-1]
        """
        
        
        # 参考思路：DP
        # dp[i]:max score from 0 to i
        n = len(nums)
        dp = [-inf] * n
        dp[0] = nums[0]
        # monotonic decreasing queue,
        # the leftmost element is largest value's INDEX
        queue = deque() 
        for i in range(1,n,1):
            # maintain the queue
            while queue and dp[queue[-1]] < dp[i-1]:
                # if the value of the rightmost index in queue
                # is smaller than that of i-1
                # discard the rightmost index 
                queue.pop()
            # append i-1 so the queue is still monotonic
            queue.append(i-1)
            
            # if the largest-valued index is less than i-1-k
            # within the k window
            # discard the first/largest-valued index
            if queue[0] <= i-1-k:
                queue.popleft()
            # update dp
            dp[i] = dp[queue[0]] + nums[i]
        return dp[-1]
        
        
# @lc code=end

