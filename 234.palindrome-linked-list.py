#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ################# 两遍遍历 passed ##############
        # # 第一遍：按顺序存下所有val
        # l = []
        # node = head
        # while node:
        #     l.append(node.val)
        #     node = node.next
        # # 第二遍：倒着对应每一个元素（双指针）
        # left, right = 0, len(l)-1
        # while left < right:
        #     if l[left] != l[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True
        # # return l == l[::-1]
        # # Time O(n) | Memory O(n)
        
        ############### 快慢指针，反转复原list ##########
        if head is None:
            return True
        
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next
            
        first_half_end.next = self.reverse_list(second_half_start)
        return result
        
        
    def end_of_first_half(self,head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse_list(self,head):
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        
    # Time O(n) | memory O(1)

# @lc code=end

