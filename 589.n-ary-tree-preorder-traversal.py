#
# @lc app=leetcode id=589 lang=python
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        self.helper(root,ans)
        return ans
        
    def helper(self,node,ans):
        if node:
            ans.append(node.val)
            if node.children:
                for child in node.children:
                    self.helper(child, ans)
# @lc code=end

