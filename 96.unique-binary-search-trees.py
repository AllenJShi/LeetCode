#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ### BST 左边比parent小，右边比parent大
            
        ############ 参考答案 ##############
        ########### 动态规划 
        G = [0] * (n+1)
        G[0], G[1] = 1, 1
        # i表示子树序列的长度
        for i in range(2, n+1):
            for j in range(1, i+1):
                # 左子树的数量乘以右子树的数量
                G[i] += G[j-1] * G[i-j]
        return G[n]
    
    
        ########### 数学
        # C = 1
        # for i in range(0,n):
        #     C = C*2*(2*i+1) / (i+2)
        # return int(C)
        
# @lc code=end

