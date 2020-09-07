# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getSize(self, root):
        size = 0
        ptr = root
        while ptr:
            size += 1
            ptr = ptr.next
        return size
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # First get the size of the linked list in O(n)
        # Then calculate the remainder of size divided by k
        # partition the link list according to k, making first groups larger according to remainder
        
        # getting the size
        size = self.getSize(root)
        remainder = size % k
        groupSize = size // k
        print(size, remainder, groupSize)
        parts = []
        ptr = root
        for _ in range(k):
            prv = None
            partRoot = ptr
            i = 0
            # adding the required amount for each part
            while ptr and i < groupSize:
                prv = ptr
                ptr = ptr.next
                i += 1
            # adding the extra values if needed
            if remainder > 0 and ptr:
                remainder -= 1
                prv = ptr
                ptr = ptr.next
            
            parts.append(partRoot)
            if prv:
                newRoot = prv.next
                prv.next = None
                ptr = newRoot
        return parts
                
        