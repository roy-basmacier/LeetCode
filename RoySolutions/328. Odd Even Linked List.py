# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        evenHead = head.next
        oddptr = head
        evenptr = head.next
        while evenptr and evenptr.next:
            oddptr.next = evenptr.next
            oddptr = oddptr.next 
            
            evenptr.next = oddptr.next
            evenptr = evenptr.next
            

        oddptr.next = evenHead
        return head