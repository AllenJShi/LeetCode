#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    
        ################# 我的答案 passed ###############
        # # 若不相等长度，必然False
        # if len(s) != len(t): return False
        
        # # 用第一个单词创建一个hashtable，字母：出现次数
        # # 用第二个单词逐项对应hashtable中的元素并-1
        # # 若出现没有的字母，则证明False
        # # 若全部通过，最后看hashtable里是否有不等于0
        # hashtable = {}
        # for char in s:
        #     if char not in hashtable.keys():
        #         hashtable[char] = 1
        #     else:
        #         hashtable[char] += 1
        
        # for char in t:
        #     if char not in hashtable.keys():return False
        #     hashtable[char] -= 1
            
        # if any(hashtable.values()):
        #     return False
        # else:
        #     return True
        
        
        ################# 参考答案 ##################
        # ############### 排序 ###################
        
        # # 若不相等长度，必然False
        # if len(s) != len(t): return False
        
        # s_arr = [i for i in s]
        # t_arr = [j for j in t]
        
        # s_arr.sort(); t_arr.sort()
        # return s_arr == t_arr
    
        ############### 哈希表 #################
        # 与我的答案大同小异
        
        
# @lc code=end

