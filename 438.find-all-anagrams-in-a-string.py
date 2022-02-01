#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        ################## 我的答案（超时）####################
        # def charSum(string):
        #     return sum(map(lambda x:ord(x),string))
        # n, m = len(s), len(p)
        # ans = []
        # for start in range(n):
        #     j = start
        #     while j < n and j-start < m and s[j] in p:
        #         j += 1
        #     if j-start == m and charSum(s[start:j])==charSum(p):
        #         ans.append(start)
        # return ans
    
        ################ Sliding window （超时）################
        n, m = len(s), len(p)
        ans = []
        # 建立两个哈希表，分别跟踪s sliding window和p字母频率
        shash = {i:0 for i in range(26)}
        phash = {i:0 for i in range(26)}
        if n < m: return ans
        left, right = 0, 0
        # 先将p的频率储存，同时游历s的前m个字段
        while right != m:
            shash[ord(s[right])-ord('a')] += 1
            phash[ord(p[right])-ord('a')] += 1
            right += 1
        # 开始游历s的后序字段
        while right < n:
            # 第一步检查上一个sliding window的频率是否与p相同
            if shash == phash:
                ans.append(left)
            # 下一个window的start
            shash[ord(s[right])-ord('a')] += 1
            # 上一个window的start，将上一个window中的字段逐个递减
            shash[ord(s[left])-ord('a')] -= 1
            # window向前推进
            right += 1
            left += 1
        # 考察最后m个字母的pinlv是否与p相同
        if shash == phash:
            ans.append(left)
        return ans
        # time O(n) | space O(1)
        
"""def findAnagrams(self, s: str, p: str) -> List[int]:
        
        solution = []
        
        # Stores the differences for each char between the counts in the sliding window and p
        # a positive entry k means that in the window there are k occurrences of that char missing compared to p
        # a negative entry k means that in the window there are k occurrences of that char in excess compared to p
        diff_cnts = defaultdict(int)
        for c_p in p:
            diff_cnts[c_p] = diff_cnts[c_p] + 1
            
        # Integer that keeps track of how many differences there are in the two strings 
        num_diff = len(p)
        for c_s in s[:len(p)]:
            if c_s in diff_cnts:
                diff_cnts[c_s] -= 1
                # if while decreasing the count for that char we go below zero
                # this means that we have one occurrence more of that char in our window
                # hence the difference should not decrease
                num_diff -= 1 if diff_cnts[c_s] >= 0 else 0
                
        if num_diff == 0:
                solution.append(0)
  
        for idx_c_s in range(1, len(s)-len(p)+1):

            c_s = s[idx_c_s - 1]
            if c_s in diff_cnts:
                diff_cnts[c_s] += 1
                
                # If we are incrementing the count from a negative number this means that 
                # we are deleting an excess in the window for that particular char, hence difference
                # do not increase
                num_diff += 1 if diff_cnts[c_s] > 0 else 0
                
            
            c_s = s[idx_c_s + len(p) - 1]
            if c_s in diff_cnts:
                diff_cnts[c_s] -= 1
                num_diff -= 1 if diff_cnts[c_s] >= 0 else 0

            if num_diff == 0:
                solution.append(idx_c_s)
                
        return solution
        """
# @lc code=end

