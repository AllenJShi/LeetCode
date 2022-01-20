#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ############# 动态规划 #################
        n = len(s)
        dp = [False] * (n+1)
        # 初始化：空字符可以被任意表示
        dp[0] = True
        for i in range(n):
            for j in range(i+1,n+1):
                if dp[i]==True and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]
        
        
        ################ DFS (case 35 超出运行范围) ###################
        # n = len(s)
        # def dfs(start):
        #     if start == n: return True
        #     for i in range(start+1,n+1):
        #         prefix = s[start:i]
        #         if prefix in wordDict and dfs(i):
        #             return True
        #     return False
        # return dfs(0)
        
        ######### 优化：加入记忆 case 35超出running time
        # n = len(s)
        # memory = [False]*n
        # def dfs(start):
        #     # if start == n: return True
        #     # if memory[start]: return memory[start]
        #     if start == n or memory[start]: return True
        #     for i in range(start+1,n+1):
        #         prefix = s[start:i]
        #         if prefix in wordDict and dfs(i):
        #             memory[start] = True
        #             return True
        #     # memory[start]不变
        #     return False
        # return dfs(0)
        
               
        ########### 回溯 （深度太大，超出运行范围）##############
        # import functools
        # @functools.cache(None)        
        # def backtracking(string):
        #     if not string: return True
        #     res=False
        #     for i in range(1,len(string)+1):
        #         if s[:i] in wordDict:
        #             res = backtracking(s[i:]) or res
        #     return res
        # return backtracking(s)
        
        
        ############### BFS case 35 超出running time范围 #####################
        # n = len(s)
        # queue = []
        # queue.append(0)
        
        # while queue:
        #     start = queue.pop(0)
        #     for i in range(start+1,n+1):
        #         prefix = s[start:i]
        #         if prefix in wordDict:
        #             if i < n:
        #                 queue.append(i)
        #             else:
        #                 return True
        # return False
        
        ############ 优化：加入记忆
        # n = len(s)
        # queue = []
        # queue.append(0)
        # visited = [False] * n
        # while queue:
        #     start = queue.pop(0)
        #     if visited[start]: continue
        #     visited[start] =  True
        #     for i in range(start+1,n+1):
        #         prefix = s[start:i]
        #         if prefix in wordDict:
        #             if i < n:
        #                 queue.append(i)
        #             else:
        #                 return True
        # return False
# @lc code=end

