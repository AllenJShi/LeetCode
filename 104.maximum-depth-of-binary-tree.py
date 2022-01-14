#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ################### DFS迭代 ######################
        # if not root:
        #     return 0
        
        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)
        
        # return max(left,right) + 1
    
    
        ################### BFS #######################
        if not root:
            return 0
        queue = []
        queue.append(root)
        depth = 0
        while queue:
            n = len(queue)
            while n>0:
                node = queue[0]
                queue = queue[1:]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                n -= 1
            depth += 1
        return depth
        
# @lc code=end

