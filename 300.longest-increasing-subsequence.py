#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ########### DP ###############
        # n = len(nums)
        # dp = [0] * (n)
        # dp[0] = 1
        # for i in range(1,n):
        #     # i本身就是一个单位的sub
        #     dp[i] = 1
        #     # 从0到i-1
        #     for j in range(0,i):
        #         # 如果对于每一个i之前的j，存在i大于j的情况
        #         if nums[i] > nums[j]:
        #             # dp更新为当前的dpi或dpj加上一个1中的max
        #             dp[i] = max(dp[i],dp[j]+1)
        # return max(dp)
        
        ########### Greedy + Binary Search ################
        ####### 思路：希望上升的慢，这样总共长度不变，子长度可能会更长
        # 维护一个数组 d[i] 记录长度为i的末尾最小值
        # d是单调递增的
        d = []
        for n in nums:
            # 若当前num比之前最长长度的末尾元素大，当前num可以被加在之前的长度后
            if not d or n > d[-1]:
                d.append(n)
            else:
                # 否则，向前寻找第一个比当前num小的末尾元素
                # 二分查找d，因为d代表每个长度的最末尾元素
                # 如果找到那个仅次于当前num的末尾元素，那么当前元素将是d中r的下一个
                l, r = 0, len(d) - 1
                loc = l
                while l <= r:
                    mid = (l+r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)
# @lc code=end

