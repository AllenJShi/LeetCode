#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        ############## DFS solution ################
        # if root.right: self.bstToGst(root.right)
        # self.val += root.val
        # root.val = self.val
        # if root.left: self.bstToGst(root.left)
        # return root
    
        ############### BFS solution ################
        curr = root
        val = 0
        while curr:
            if curr.right:
                leftmost = curr.right
                while leftmost.left and leftmost.left!=curr:
                    leftmost = leftmost.left
                    
                if not leftmost.left:
                    leftmost.left = curr
                    curr = curr.right
                else:
                    leftmost.left = None
                    val += curr.val
                    curr.val = val
                    curr = curr.left
            else:
                # when there no more right child
                # => no more nodes greater than curr
                val += curr.val
                curr.val = val
                curr = curr.left
        return root
        
# @lc code=end

