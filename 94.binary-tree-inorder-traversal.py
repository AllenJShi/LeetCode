#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ############## METHOD OF WHITE-GRAY ##################
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        white,gray = 0,1
        res = []
        stack = [(root,white)]
        while stack:
            node, color = stack.pop()
            if node is None: continue
            if color == white:
                stack.append((node.right, white))
                stack.append((node, gray))
                stack.append((node.left, white))
            else:
                res.append(node.val)
        return res
    
    ####################### METHOD OF RECURSION ##################
    def inorderTraversal(self, root):

        array = []
        def helper(root,array):
            if root is not None:
                helper(root.left, array)
                array.append(root.val)
                helper(root.right, array)
            return array
        
        return helper(root,array)
        
# @lc code=end

