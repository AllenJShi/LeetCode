#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # base case: if empty tree
        if not root:
            return True
        
        # 用104题中的maxdepth查找每一个subtree的最大深度
        # 两棵subtree的最大深度小于等于1就符合要求
        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            if left == -1: return -1
            right = maxDepth(root.right)
            if right == -1: return -1
            return max(left,right)+1 if abs(left-right) < 2 else -1
        
        return False if maxDepth(root)==-1 else True
        
# @lc code=end

