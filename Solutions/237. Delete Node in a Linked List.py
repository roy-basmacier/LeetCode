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
        # Time complexity O(N)
        # nextNode = node.next
        # prvNode = node
        # while nextNode:
        #     node.val = nextNode.val
        #     prvNode = node
        #     node = nextNode
        #     nextNode = nextNode.next
        # prvNode.next = None # deletes the last element
        
        # Time Complexity O(1)
        node.val = node.next.val
        node.next = node.next.next