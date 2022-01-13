#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        q = deque()
        q.append(root)
        row = 0 
        while q:
            level = []
            row += 1
            l2r = row%2
            for _ in range(len(q)):
                if l2r==1:
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    node = q.pop()
                    level.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
            ans.append(level)
        return ans
# @lc code=end

