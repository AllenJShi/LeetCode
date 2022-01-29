#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ############# 我的答案 ################
        # hashmap={num:0 for num in nums}
        # for i, num in enumerate(nums):
        #     hashmap[num] += 1
        # ans = []
        # while k > 0:
        #     largest = max(hashmap.values())
        #     for num in hashmap:
        #         if (hashmap[num] == largest) and (num not in ans):
        #             ans.append(num)
        #             del hashmap[num]
        #             k -= 1
        #             break
        # return ans
        
        # time O(nk) | space O(n)
        
        ################# heap ################
        import heapq
        hashmap={num:0 for num in nums}
        for i, num in enumerate(nums):
            hashmap[num] += 1
        pri_que = []
        for key, freq in hashmap.items():
            heapq.heappush(pri_que, (freq,key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        result = [0] * k
        for i in range(k-1,-1,-1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
            
# @lc code=end

