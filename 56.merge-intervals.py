#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
               
        ############## 我的答案 time O(n^2 + logn) | space O(n) ###############
        """Constraints:

            1 <= intervals.length <= 104
            intervals[i].length == 2
            0 <= starti <= endi <= 104
        """
        # ans = []
        # used = [False] * len(intervals)
        # # sorted by the first element
        # intervals.sort()
        # for i,interval in enumerate(intervals):
        #     if used[i]: continue
        #     [lower,upper] = interval
        #     used[i] = True
        #     for j, nextInt in enumerate(intervals[i+1:]):
        #         if upper >= nextInt[0] and not used[i+j+1]:
        #             upper = max(upper,nextInt[1])
        #             used[i+j+1] = True
        #     ans.append([lower,upper])
        # return ans
    
    
        ################ 参考答案 ##############
        # 与我的思路相同，代码更简单
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])        
        return merged
    
        # time O(nlogn) | space O(logn)
        
        
# @lc code=end

