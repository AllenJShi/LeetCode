#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ############## 前缀和 + 哈希表 #############
        ans = 0
        prefix = 0
        hashmap = collections.defaultdict(int)
        hashmap[0] = 1
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in hashmap:
                ans += hashmap[prefix-k]
            hashmap[prefix] = hashmap[prefix] + 1 if hashmap[prefix] else 1
        return ans
# @lc code=end

