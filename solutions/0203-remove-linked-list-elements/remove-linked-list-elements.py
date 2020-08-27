# -*- coding:utf-8 -*-


# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur = head
        prv = None
        while cur and cur.val == val:
            head = cur.next
            cur.next = None
            cur = head
        
        while cur:
            if cur.val == val:
                prv.next = cur.next
                cur.next = None
                cur = prv
            prv = cur
            cur = cur.next
        return head
                    
                
