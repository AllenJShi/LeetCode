#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            # empty list
            return
        if not head.next:
            # len of 1
            return TreeNode(head.val)
        
        Lstack, Rstack = [], []
        
        
        tmp = head.next
        length =1
        while tmp:
            length += 1
            tmp = tmp.next
        mid = length // 2
        print(length, mid)
            
        pos = 0
        while pos < mid and head:
            Lstack.append(head.val)
            head = head.next
            pos += 1
        print(pos, head.val)
        res = TreeNode(head.val)
        pos += 1
        head = head.next
        while head:
            Rstack.append(head.val)
            head = head.next
            # pos += 1
        print(Lstack,Rstack)
        dummyTree = TreeNode(left=res)
        while Lstack:
            v = Lstack.pop()
            res.left = TreeNode(val=v)
            res = res.left
        if not Rstack:
            return dummyTree.left
        res = dummyTree.left
        v = Rstack.pop()
        res.right = TreeNode(val=v)
        res = res.right
        while Rstack:
            v = Rstack.pop()
            res.left = TreeNode(val=v)
            res = res.left
        return dummyTree.left
# @lc code=end

