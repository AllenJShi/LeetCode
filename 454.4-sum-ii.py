#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = collections.defaultdict(int)
        count = 0
        # two sum storing all possible summation frequency
        for i in nums1:
            for j in nums2:
                hashmap[i+j] += 1
        # print(hashmap)
        # check if 3 and 4 can constitute the remaining part
        for p in nums3:
            for q in nums4:
                count += hashmap[0-p-q]
        return count
# @lc code=end

