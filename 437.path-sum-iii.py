#
# @lc app=leetcode id=437 lang=python
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        ############# DFS ###################
        # def backtracking(root,targetSum):
        #     if not root: return 0 
        #     res = 0        
        #     if root.val == targetSum:
        #         res += 1
        #     res += backtracking(root.left, targetSum - root.val)
        #     res += backtracking(root.right, targetSum - root.val)
        #     return res
        # if not root: return 0
        # res = backtracking(root,targetSum)
        # res += self.pathSum(root.left, targetSum)
        # res += self.pathSum(root.right, targetSum)
        # return res
    
        # time O(N^2) | space O(N)
        
        ############### 前缀和 ####################
        #######思路：当前元素的路径之和
        # 记录从root到当前结点除当前节点外的前缀和
        prefixSum = collections.defaultdict(int)
        # 若curr-rootval=0，这里必然有一个path包括root自己
        prefixSum[0] = 1
        
        def backtracking(root,curr):
            # 终止条件
            if not root: return 0
            res = 0
            # 前缀和加上当前结点的val
            curr += root.val
            # 从之前的前缀和中寻找
            res += prefixSum[curr-targetSum]
            # 前缀和为curr时，更新一条路径
            prefixSum[curr] += 1
            # 搜索左子树
            res += backtracking(root.left,curr)
            # 搜索右子树
            res += backtracking(root.right,curr)
            # 回溯
            prefixSum[curr] -= 1
            return res
        return backtracking(root,0)
        
        # time O(n) | space O(n)
        
        
# @lc code=end

