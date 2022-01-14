#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ############ 快慢指针 O(1) ###################
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            # 若快指针提前进入的尾端，而过程中慢指针没有追上
            # 则判断无环
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
            
        # 跳出循坏的条件是快慢指针相遇，即出现cycle
        return True
        
# @lc code=end

