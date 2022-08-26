#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # # dfs solution
        
        # # maintain a dict with level:maxval
        # max_val = {} 
    
        # def dfs(node, level):
        #     if not node: return
        #     max_val[level] = max(node.val, max_val[level]) if level in max_val else node.val
        #     dfs(node.left, level+1)
        #     dfs(node.right, level+1)
           
        # dfs(root,0) 
        # # sort by key
        # max_val = sorted(max_val.items(),key=lambda x:x[0])
        # # return values sorted by keys (levels)
        # return list(map(lambda x:x[1],max_val))
        
        
        
        
        # bfs solution
        queue =deque([root])
        res = []
        while queue:
            max_val = float('-inf')
            for _ in range(len(queue)):
                # pop out all nodes in same level
                node = queue.popleft()
                # if null, then continue next node
                if not node: continue
                # get the max on the same level
                max_val = max(max_val,node.val)
                # add child nodes
                queue.extend([node.left,node.right])
            if max_val != float('-inf'):
                res.append(max_val)
        return res
        
        
# @lc code=end

