#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def preOrderTraverse(tree,array):
            if tree is not None:
                array.append(tree.val)
                preOrderTraverse(tree.left,array)
                preOrderTraverse(tree.right,array)

        array = []
        preOrderTraverse(root,array)
        array.sort()

        return array[k-1]
    
    

        
        
# @lc code=end

