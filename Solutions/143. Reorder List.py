# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)
        if not head:
            return
        stack = [] # (prvNode, endNode)
        ptr = head
        while ptr.next:
            stack.append((ptr, ptr.next))
            ptr = ptr.next
        
        startPtr = head
        while startPtr and stack:
            # pop the last nodes from our stack
            prvPtr, endPtr = stack.pop()
            
            if startPtr == endPtr or prvPtr == startPtr:
                break
                
            # Do the arrangement
            endPtr.next = startPtr.next
            startPtr.next = endPtr
            if prvPtr:
                prvPtr.next = None
            
            # Iterate startPtr
            startPtr = endPtr.next
        
        '''
        # Time Compelxity -> O(n^2)
        # Space Complexity -> O(1)
        
        startPtr = head
        while startPtr:
            # We will find the last node in the list and the one before it
            prvPtr = None
            endPtr = startPtr
            # Go to the end of the list
            while endPtr.next:
                prvPtr = endPtr
                endPtr = endPtr.next
            
            if startPtr == endPtr or prvPtr == startPtr:
                break
            # Do the rearrangement
            endPtr.next = startPtr.next
            startPtr.next = endPtr
            if prvPtr:
                prvPtr.next = None
            
            # Repeat for next node (skipping the newly placed node)
            startPtr = endPtr.next
        '''
                
        
        