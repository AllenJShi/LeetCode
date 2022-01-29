#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # ############ DP （时间不允许） ##############
        # dp = [float('inf')] * (n+1)
        # dp[0] = 0
        # for i in range(n+1):
        #     for j in range(1,i+1):
        #         # 定义当前平方数，若大于dp的i，直接中断
        #         v = j**2
        #         if v > i:
        #             break
        #         # 能达到i的最小平方数是，之前最小的记忆或加上当前平方数后
        #         dp[i] = min(dp[i],dp[i-v]+1)
        # return dp[n]
        
        
        
        ########## 图 #############
        ### 思路：
        # n到0每一个数字代表一个node
        # 若两节点可以被一个平方数连接，则连一条edge
        # 构成directed unweighted graph
        # eg. 6|---4--->2|---1--->1|---1--->0
        # 6 = 4+1+1
        
        # class Node:
        #     def __init__(this,first,second):
        #         this.first = first
        #         this.second = second
        
        # queue = collections.deque()
        # visited = [False] * (n+1)
        # queue.append(Node(n,0))
        # visited[n] = True
        
        # while queue:
        #     # pop开头节点
        #     node = queue.popleft()
        #     # num是当前结点的值
        #     num = node.first
        #     # step是从n到num所需经历的edge
        #     step = node.second
        #     # 如果当前到0，说明已经找到所有的n到0的途径，ie 平方数
        #     if num==0: return step
        #     i = 1
        #     while True:
        #         a = num - i*i
        #         # 若平方数本身大于当前结点的值num，跳出while，代表当前结点的邻居结点已找全
        #         if a < 0:break
        #         # 把邻居结点依次加入队列
        #         if not visited[a]:
        #             # 同一结点的相邻结点（广度搜索）拥有相同个数的平方数（edges）
        #             queue.append(Node(a, step+1))
        #             visited[a] = True
        #         i += 1
        # return 0
    
        ################ DP (时间允许) #############
        dp = [0] * (n+1)
        for i in range(1,n+1):
            minimum, k = i, 1
            while i-k*k >= 0:
                minimum = min(dp[i-k*k],minimum)
                k+=1
            dp[i] = minimum + 1
        return dp[n]
# @lc code=end

