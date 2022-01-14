#
# @lc app=leetcode id=237 lang=python
#
# [237] Delete Node in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ######### 我的答案 passed ##############
        # while node.next and node.next.next:
        #     node.val = node.next.val
        #     node = node.next
        # node.val = node.next.val
        # node.next = None
                
        ############ 参考答案 #############
        # 直接与下一个节点交换,跳过/删除下一节点
        node.val = node.next.val
        node.next = node.next.next
        
# @lc code=end

