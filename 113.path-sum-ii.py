#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(root, s):
            if not root:
                return
            path.append(root.val)
            s -= root.val
            if not root.left and not root.right and s==0:
                # 左右子树都已经到头，并且path sum
                res.append(path[:])
            dfs(root.left,s)
            dfs(root.right,s)
            # 路径回到上一层
            path.pop()
        dfs(root, targetSum)
        return res


# @lc code=end

