#
# @lc app=leetcode id=337 lang=python
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ################ DFS ####################
        chosen = collections.defaultdict(int)
        notchosen = collections.defaultdict(int)
        
        def backtracking(root):
            if not root: return
            backtracking(root.left)
            backtracking(root.right)
            chosen[root] = root.val + notchosen[root.left] + notchosen[root.right]
            notchosen[root] = max(chosen[root.left],notchosen[root.left]) \
                + max(chosen[root.right],notchosen[root.right])
            
        backtracking(root)
        return max(chosen[root],notchosen[root])
    
    # time O(n) | space O(n)
# @lc code=end

