#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ################### 学习前抄的答案（passed）############
        # ans = []
        # num = 4
        # address = [0] * num
        
        # def dfs(key,start):
        #     if key == num:
        #         #当我们已经发现所有的四段IP后，
        #         #若string中start的位置就是在末尾，即可放心的将四段IP用.连接
        #         if start == len(s):
        #             ip = '.'.join(str(add) for add in address)
        #             ans.append(ip)
        #         return
            
        #     if start == len(s):
        #         #若检测到start的位置就是string的末尾，
        #         #但是可能并没有四段完整的IP，则invalid，直接返回，放弃该尝试
        #         return
            
        #     if s[start] == '0':
        #         #检测到start的位置是0时，我们知道0不可为开头，
        #         #所以0本身必为一段IP，我们可以将它独立放进IP字段中，然后从下一个位置再开始
        #         address[key] = 0
        #         dfs(key+1, start+1)
                
        #     #普遍情况下
        #     add = 0
        #     for end in range(start, len(s)):
        #         add = add * 10 + (ord(s[end])-ord('0'))
        #         if 0 < add <= 0xFF:
        #             #当add在0和255之间是，被认定为合规的IP字段
        #             address[key] = add
        #             dfs(key+1, end+1)
        #         else:
        #             #字段不合规，不予更新
        #             break
                    
        # dfs(0,0)
        # return ans
        
        ##################### 我的成果（passed）###################
        ans = []
        n = 4
        path = []
        
        if len(s) > 12:
            return []
        
        def backtracking(idx):
            if len(path) == n:
                if idx == len(s):
                    ans.append(".".join(path[:]))
                    return
            
            for i in range(idx+1,len(s)+1):
                substring = s[idx:i]
                if not 0 <= int(substring) <= 255:
                    continue
                if not substring=='0' and not substring.lstrip('0')==substring:
                    continue
                path.append(substring)
                backtracking(i)
                path.pop()
                
        backtracking(0)
        return ans
                 
            
            
    
        
# @lc code=end

