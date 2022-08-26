#
# @lc app=leetcode id=971 lang=python3
#
# [971] Flip Binary Tree To Match Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        """the left subtree and rigth subtree"""
        stack = [root] # stack keep the order of push-in
        # queue not work because the root will be visited first
        res = []
        i = 0
        while stack:
            curr = stack.pop()
            if not curr: # if curr is None, it is leaf node
                continue
            if curr and curr.val!=voyage[i]:
                return [-1]
            i += 1
            # because of pre-order, check the right first
            # if right match with i, then flip subtrees
            if curr.right and curr.right.val==voyage[i]:
                # check left is necessary!
                # otherwise, you flip a None left tree
                if curr.left:
                    res.append(curr.val)
                stack.extend([curr.left,curr.right]) # left, right but right is popped out first
            else:
                stack.extend([curr.right,curr.left])
        return res
    
        
# @lc code=end

