#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        ############### 回溯，哈希 ###############
        # # 随机指针指向的node可能还没有建立
        # # 需要用哈希表记录，然后回溯
        # if not head: return None
        # hashmap = dict()
        # if not hashmap.get(head):
        #     chead = Node(head.val)
        #     hashmap[head] = chead
        #     chead.next = self.copyRandomList(head.next)
        #     chead.random = self.copyRandomList(head.random)
        # return hashmap[head]
    
        ############### 迭代 ###############
        if not head: return None
        node = head
        while node:
            cnode = Node(node.val)
            cnode.next = node.next
            node.next = cnode
            node = node.next.next
        
        node = head
        while node:
            cnode = node.next
            cnode.random = node.random.next if node.random else None
            
        chead = head.next
        while head:
            cnode = head.next
            head.next = head.next.next
            cnode.next = cnode.next.next if cnode.next else None
        return chead 
                    
# @lc code=end

