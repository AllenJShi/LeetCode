#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        tmpNode = TreeNode(val=float(-inf))
        
        def dfs(node):
            # must globalize vars in function python3
            nonlocal first, second, tmpNode
            if not node: return
            
            dfs(node.left)
            
            if not first and tmpNode.val >= node.val:          
                first = tmpNode
            if first and tmpNode.val >= node.val:
                second = node
                
            tmpNode = node
            
            dfs(node.right)
        
        dfs(root)
        
        first.val, second.val = second.val, first.val
# @lc code=end

