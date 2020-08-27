# -*- coding:utf-8 -*-


# Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.
#
# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
#
# It is guaranteed that the answer will in the range of 32-bit signed integer.
#
# Example 1:
#
#
# Input: 
#
#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 
#
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
#
#
# Example 2:
#
#
# Input: 
#
#           1
#          /  
#         3    
#        / \       
#       5   3     
#
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
#
#
# Example 3:
#
#
# Input: 
#
#           1
#          / \
#         3   2 
#        /        
#       5      
#
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
#
#
# Example 4:
#
#
# Input: 
#
#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
#
#
#  
# Constraints:
#
#
# 	The given binary tree will have between 1 and 3000 nodes.
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # keep two hashmaps
        # Height -> maxDistance
        # Height -> minDistance
        maxDist = {}
        minDist = {}
        def helper(node, h, d):
            if not node:
                return
            if h not in maxDist:
                maxDist[h] = d
                minDist[h] = d
            else:
                maxDist[h] = max(maxDist[h], d)
                minDist[h] = min(minDist[h], d)

            
            if node.left:
                helper(node.left, h + 1, (d * 2)-1)
            if node.right:
                helper(node.right, h + 1, d * 2)
                
                
        helper(root, 0, 1)
        res = 0
        for h in maxDist.keys():
            res = max(res, maxDist[h] - minDist[h] + 1) 
        return res
            
