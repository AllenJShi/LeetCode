#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ############ DFS solution ##############
        # nums = []
        
        # def dfs(curr,res):
        #     if (not curr.left and not curr.right):
        #         nums.append(res)
        #         return
        #     if curr.left:
        #         dfs(curr.left,res+str(curr.left.val))
        #     if curr.right:
        #         dfs(curr.right,res+str(curr.right.val))
        
        # dfs(root,str(root.val))
        
        # return sum(map(int,nums))
        
        
        
        ########### BFS solution ###########
        res, queue = 0, deque([root])
        while queue:
            curr = queue.popleft()
            
            # only values of leaves will be added
            if not curr.left and not curr.right:
                res += curr.val
                
            # increment value for all ascending nodes
            if curr.left:
                curr.left.val += curr.val*10
                queue.append(curr.left)
            if curr.right:
                curr.right.val += curr.val*10
                queue.append(curr.right)
        return res
    
            
        
# @lc code=end

