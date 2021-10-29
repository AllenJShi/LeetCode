#
# @lc app=leetcode id=590 lang=python
#
# [590] N-ary Tree Postorder Traversal
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
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        self.helper(root,ans)
        return ans
        
    def helper(self,node,ans):
        if node:
            if node.children:
                for child in node.children:
                    self.helper(child, ans)
            ans.append(node.val)
        
# @lc code=end

