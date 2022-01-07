#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ############## Recursion ################
        # def helper(node, low=float('-inf'), high=float('inf')):
        #     if not node:
        #         return True
            
        #     val = node.val
        #     if val <= low or val >= high:
        #         return False
            
        #     if not helper(node.left, low, val):
        #         return False
            
        #     if not helper(node.right, val, high):
        #         return False
            
        #     return True
        
        # return helper(root)
        
        
        ################## Traversal ################
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
            
        return True        
        
# @lc code=end

