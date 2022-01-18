#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        def validAnagrams(s,t):
            # 若不相等长度，必然False
            if len(s) != len(t): return False
            
            s_arr = [i for i in s]
            t_arr = [j for j in t]
            
            s_arr.sort(); t_arr.sort()
            return s_arr == t_arr
        
        # 超时
        # used = []
        # ans = []
        # for i in range(len(strs)):
        #     if strs[i] in used: continue
        #     subans = [strs[i]]
        #     used.append(strs[i])
        #     for j in range(i+1,len(strs)):
        #         if validAnagrams(strs[i],strs[j]):
        #             subans.append(strs[j])
        #             used.append(strs[j])
        #     ans.append(subans)
        # return ans
        
        ################# 参考答案 ###################
        # ########## 哈希 ###############
        # # 用list作为hash表的value，eg. {x:[],...}
        # # tuple表示26个字母在string中出现的次数
        # hashmap = collections.defaultdict(list)
        # for each in strs:
        #     counts = [0] * 26
        #     for char in each:
        #         counts[ord(char)-ord('a')] += 1
        #     hashmap[tuple(counts)].append(each)
        # return list(hashmap.values())
        
        ############# 排序 ################
        hashmap = collections.defaultdict(list)
        for each in strs:
            key = "".join(sorted(each))
            hashmap[key].append(each)
        return list(hashmap.values())
# @lc code=end

