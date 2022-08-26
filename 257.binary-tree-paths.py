#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ########### DFS solution ############
        # res = []
        # def dfs(curr,s):
        #     if not curr.left and not curr.right:
        #         res.append(s)
        #         return
        #     if curr.left:
        #         dfs(curr.left,s+"->"+str(curr.left.val))
        #     if curr.right:
        #         dfs(curr.right,s+"->"+str(curr.right.val))
        # dfs(root,str(root.val))
        # return res
    
        ############ BFS solution ############
        res, queue = [], deque([root])
        while queue:
            curr = queue.popleft()
            if not curr.left and not curr.right:
                res.append(str(curr.val))
            if curr.left:
                curr.left.val = str(curr.val) + "->" + str(curr.left.val)
                queue.append(curr.left)
            if curr.right:
                curr.right.val = str(curr.val) + "->" + str(curr.right.val)
                queue.append(curr.right)
        return res
# @lc code=end

