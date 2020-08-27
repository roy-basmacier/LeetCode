# -*- coding:utf-8 -*-


# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
#
# Return the following binary tree:
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # inorder -> left print right
        # postorder -> left right print
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i
            
        def helper(start, end):
            if start > end:
                return None
            node = TreeNode(postorder.pop())
            rootIndex = inorder_map[node.val]
            node.right = helper(rootIndex+1, end)
            node.left = helper(start, rootIndex-1)
            return node
        return helper(0, len(inorder)-1)
        
