#
# @lc app=leetcode id=116 lang=python
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        ############## BFS #############
        if not root: return root
        # queue = [root]
        # # queue = collections.deque()
        # # queue.append(root)
        # while queue:
        #     tmp = queue[0]
        #     size = len(queue)
        #     for i in range(1,size):
        #         tmp.next = queue[i]
        #         tmp = queue[i]
        #     # BFS
        #     for _ in range(size):
        #         tmp = queue.pop(0)
        #         # tmp = queue.popleft()
        #         if tmp.left:
        #             queue.append(tmp.left)
        #         if tmp.right:
        #             queue.append(tmp.right)
        # return root
        
        ########### 改良 constant space：
        
        prev = root
        while prev.left:
            tmp = prev
            while tmp:
                tmp.left.next = tmp.right
                if tmp.next:
                    tmp.right.next = tmp.next.left
                tmp = tmp.next
            prev = prev.left  
        return root
        
        

        ############### 递归 ###############
        # def helper(current_root):
        #     # 终止条件：当前root是最底层
        #     if not current_root:
        #         return
        #     # 左节点不断向右
        #     # 右节点不断向左
        #     left_tree = current_root.left
        #     right_tree = current_root.right
        #     while left_tree:
        #         left_tree.next = right_tree
        #         left_tree = left_tree.right
        #         right_tree = right_tree.left
        #     helper(current_root.left)
        #     helper(current_root.right)
        # helper(root) 
        # return root
                
        
        
        
# @lc code=end

