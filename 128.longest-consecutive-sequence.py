#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        You must write an algorithm that runs in O(n) time. ==》不能排序
        """
        hashmap = set(nums)
        consecutive_count = 0
        
        for num in nums:
            if num-1 not in hashmap:
                current_num = num
                current_count = 1

                while current_num + 1 in hashmap:
                    current_num += 1
                    current_count += 1
                    
                consecutive_count = max(consecutive_count, current_count)
       
        return consecutive_count
            
        # time O(n) | space O(n)
# @lc code=end

