#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # bfs solution
        if not root: return 0
        min_depth = 1 # root node itself is depth 1
        queue = [root]
        while queue:
            n = len(queue)
            while n > 0:
                curr = queue.pop(0)

                if not curr.left and not curr.right:
                    return min_depth
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                n -= 1
                
            min_depth += 1
        
        return 0
        
        
        # # dfs solution
        # if not root: return 0
        # if not root.left and not root.right:
        #     return 1
        # if not root.left:
        #     return 1 + self.minDepth(root.right)
        # if not root.right:
        #     return 1 + self.minDepth(root.left)
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
        
        # version 2
        if not root: return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l==0 or r==0:
            return 1 + l + r
        else:
            return 1 + min(l,r)
# @lc code=end

