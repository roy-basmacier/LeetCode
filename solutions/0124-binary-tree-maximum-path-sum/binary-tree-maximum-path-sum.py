# -*- coding:utf-8 -*-


# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# Example 1:
#
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
#
#
# Example 2:
#
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root.left and not root.right:
            return root.val
        def helper(node):
            if not node:
                return [float('-inf')] * 2
            
            leftSum = helper(node.left)
            rightSum = helper(node.right)
            
            return [node.val + max(leftSum[0], rightSum[0], 0), max(leftSum + rightSum + [node.val + leftSum[0] + rightSum[0]])]
        return max(helper(root))

        
