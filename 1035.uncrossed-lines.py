#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp, m, n = collections.defaultdict(int), len(nums1), len(nums2)
        for i in range(m):
            for j in range(n):
                dp[i, j] = max(dp[i - 1, j - 1] + (nums1[i] == nums2[j]), dp[i - 1, j], dp[i, j - 1])
        return dp[m - 1, n - 1]
# @lc code=end

