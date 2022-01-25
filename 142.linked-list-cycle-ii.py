#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ########## 我的答案 ###############
        # visited = set()
        # curr = head
        # while curr:
        #     if curr not in visited:
        #         visited.add(curr)
        #     else:
        #         return curr
        #     curr = curr.next
        # return
        
        # time O(n) | space O(n)
        
        ############ 快慢指针 #############
        fast = head
        slow = head
        while fast:
            slow = slow.next
            if not fast.next:
                return 
            fast = fast.next.next
            if fast == slow:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return
        

        # time O(n) | space O(1)
        
# @lc code=end

