#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        q = []
        q.append(root)
        while q:
            ans.append([node.val for node in q])
            level = []
            for node in q:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            q = level
        return ans
        
# @lc code=end

