#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        """ BFS solution """
        # if not root: return None
        
        # queue = deque([root])
        # # visited = set([root])
        
        # while queue:
        #     tmp = None
        #     for _ in range(len(queue)):
        #         curr = queue.popleft()
        #         curr.next = tmp
        #         tmp = curr
        #         # visited.add(curr)
        #         if curr.right:
        #             queue.append(curr.right) # right enter queue first because tmp=None initially
        #         if curr.left:
        #             queue.append(curr.left)
        # return root
        
        """ DFS solution """
        if not root: return None
        p = root.next
        while p:
            if p.left:
                p = p.left
                break
            if p.right:
                p = p.right
                break
            p = p.next
        if root.right: root.right.next = p
        if root.left: root.left.next = root.right if root.right else p
        self.connect(root.right)
        self.connect(root.left)
        return root
# @lc code=end

