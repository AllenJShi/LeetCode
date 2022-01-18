#
# @lc app=leetcode id=105 lang=python
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        ########### 迭代 #############
        # if not preorder:
        #     return None
        
        # # 根节点一定在preorder中最先被遍历
        # root = TreeNode(val=preorder[0])
        # # 维护一个栈和inorder中的指针
        # stack = [root]
        # inorderIndex = 0
        
        # # 开始遍历preorder中的节点
        # for i in range(1,len(preorder)):
        #     val = preorder[i]
        #     # 栈顶结点
        #     node = stack[-1]
        #     # 若栈顶结点和inorder中的结点不相同
        #     # 则inorder中的结点并不是当前子树的根节点
        #     # preorder中的当前结点就是栈顶结点的left
        #     if node.val != inorder[inorderIndex]:
        #         node.left = TreeNode(val=val)
        #         stack.append(node.left)
        #     else:
        #         # 若栈顶结点和inorder中的结点不相同
        #         while stack and stack[-1].val == inorder[inorderIndex]:
        #             node = stack.pop()
        #             inorderIndex += 1
        #         node.right = TreeNode(val=val)
        #         stack.append(node.right)
                
        # return root
    
        ########## 递归 ###############

        preLEN = len(preorder)
        inLEN = len(inorder)
        if preLEN != inLEN: return None
        
        hashmap = {
            val:index for index, val in enumerate(inorder)
        }   
        
        def backtracking(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight or inLeft > inRight:
                return None
            rootVal = preorder[preLeft]
            root = TreeNode(val=rootVal)
            pivotIndex = hashmap[rootVal]
            # inorder中，根节点是pivot，左子树[inLeft,pivot-1],右子树[pivot+1,inRight]
            # preorder中，根节点是preLeft，左子树[preLeft+1,pivot-inLeft+preLeft],右子树[pivot-inLeft+preLeft+1,preRight]
            root.left = backtracking(preLeft+1,pivotIndex-inLeft+preLeft,inLeft,pivotIndex-1)
            root.right = backtracking(pivotIndex-inLeft+preLeft+1,preRight,pivotIndex+1,inRight)
            return root
        
        return backtracking(0,preLEN-1,0,inLEN-1)

        # time O(n) | space O(n)
        
# @lc code=end

