#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ############### 我的答案 #################
        # # 1. 0 一定不是在开头
        # # 2. 一个数字最大不能过26
        # # 3. 每次真正影响的是最后一个和倒数第二个能否组成一个新的元素
        # if len(s) < 1 or s[0]=='0': return 0
        
        # n = len(s)
        # # 第一个元素0代表什么都没有的时候
        # dp = [0] * (n+1)
        # dp[0] = 1
        # dp[1] = 1
        # # 当有2个元素时就要开始讨论了：
        
        # for i in range(1,n):
        #     # i对应string中的index
        #     # j是对应的在dp中的index
        #     j = i+1

        #     # 若，最后一个为0，只考虑与前一个和在一起是否能在1到26之间
        #     # 若条件满足（10或20），则dp[i]=dp[i-2]
        #     # 若不满足（不在26个之中），返回0结束
        #     if s[i] == '0':
        #         if 1 <= int(s[i-1:i+1]) <=26 and s[i-1] != '0':
        #             # print(int(s[i-1:i+1]))
        #             dp[j] = dp[j-2]
        #         else:
        #             return 0
        
        #     # 若，最后一个不为0，考虑与前一个组合在【1，26】中
        #     # 若条件满足，则dp[i] = dp[i-1] + dp[i-2]
        #     # 若不满足(不在1到26之间)，则dp[i] = dp[i-1]
        #     else:
        #         if 1 <= int(s[i-1:i+1]) <=26 and s[i-1] != '0':
        #             dp[j] = dp[j-2] + dp[j-1]
        #         else:
        #             dp[j] = dp[j-1]
                    
        # return dp[n]
        
        
        ############# 参考答案 #################
        # n = len(s)
        # f = [1] + [0] * n
        # for i in range(1,n+1):
        #     if s[i-1] != '0':
        #         f[i] += f[i-1]
        #     if i>1 and s[i-2] != '0' and int(s[i-2:i])<=26:
        #         f[i] += f[i-2]
        # return f[n]
    
        # 省去数组
        n = len(s)
        a , b, c = 0, 1, 0
        for i in range(1,n+1):
            c = 0
            if s[i-1] != '0':
                c += b
            if i>1 and s[i-2] != '0' and int(s[i-2:i])<=26:
                c += a
            a,b = b, c
        return c

        # time O(n) | space O(1)
        
        
# @lc code=end

