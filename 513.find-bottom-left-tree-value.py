#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # # bfs solution
        # queue = deque([root])
        # while queue:
        #     node = queue.popleft()
        #     # when node is leaf and no more in queue
        #     if not node.left and not node.right and not queue:
        #         return node.val
        #     # right node enters first
        #     # this guarantees the last node to 
        #     # be processed is leftmost one
        #     if node.right:
        #         queue.append(node.right)
        #     if node.left:
        #         queue.append(node.left)
                
                
                
                
        # dfs solution
        
        def dfs(node):
            # base case: the node is null
            if not node: return 0, None
            lh,lnode = dfs(node.left)
            rh,rnode = dfs(node.right)
            if lnode and rnode:
                # the equality guarantees the leftmost leaf
                return (lh+1,lnode) if lh >= rh else (rh+1,rnode)
            elif rnode:
                return (rh+1,rnode)
            elif lnode:
                return (lh+1,lnode)
            else:
                # the node is a leaf
                # both left rigth are null nodes (base)
                return 1,node
            
        return dfs(root)[1].val


                

                
                
            
                
            
                
        
# @lc code=end

