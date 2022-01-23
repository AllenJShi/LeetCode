#
# @lc app=leetcode id=114 lang=python
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        ############# 递归 ###############3
        # if not root: return []
        # res = []
        # def preorder(node):
        #     if node:
        #         res.append(node)
        #         preorder(node.left)
        #         preorder(node.right)
            
        # preorder(root) 
        # for i in range(1,len(res)):
        #     prev, curr = res[i-1], res[i]
        #     prev.left = None
        #     prev.right = curr
        
        ############ 迭代 ################
        preorderList = []
        stack = []
        node = root
        while node or stack:
            while node:
                preorderList.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
            
        for i in range(1,len(preorderList)):
            prev, curr = preorderList[i-1], preorderList[i]
            prev.left = None
            prev.right = curr
            
        # time O(n) | space O(n)
        
# @lc code=end

