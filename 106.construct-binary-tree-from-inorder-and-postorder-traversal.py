#
# @lc app=leetcode id=106 lang=python
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        ############ 递归 ################
        postLEN = len(postorder)
        inLEN = len(inorder)
        if postLEN != inLEN: return None
        
        hashmap = {
            val:index for index, val in enumerate(inorder)
        }   

        def backtracking(postLeft, postRight, inLeft, inRight):
            # 终止条件
            if postLeft > postRight or inLeft > inRight:
                return None
            rootVal = postorder[postRight]
            root = TreeNode(val=rootVal)
            pivotIndex = hashmap[rootVal]
            # inorder中，根节点是pivot，左子树[inLeft,pivot-1],右子树[pivot+1,inRight]
            root.left = backtracking(postLeft,pivotIndex-inLeft+postLeft-1,inLeft,pivotIndex-1)
            root.right = backtracking(pivotIndex-inLeft+postLeft,postRight-1,pivotIndex+1,inRight)
            return root
        
        return backtracking(0,postLEN-1,0,inLEN-1)
# @lc code=end

