# -*- coding:utf-8 -*-


# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
#
#  
#
#  
# Example 1:
#
#
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
#
#
# Example 2:
#
#
# Input: root = [1,2,3]
# Output: [1,3]
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
# Example 4:
#
#
# Input: root = [1,null,2]
# Output: [1,2]
#
#
# Example 5:
#
#
# Input: root = []
# Output: []
#
#
#  
# Constraints:
#
#
# 	The number of the nodes in the tree will be in the range [1, 104].
# 	-231 <= Node.val <= 231 - 1
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        depth = {} # depth -> max value
        queue = [(root, 0)]
        while queue:
            node, dep = queue[0]
            queue = queue[1:]
            if dep not in depth:
                depth[dep] = node.val
            depth[dep] = max(node.val, depth[dep])
            if node.left:
                queue.append((node.left, dep + 1))
            if node.right:
                queue.append((node.right, dep + 1))
        res = []
        for key, val in depth.items():
            res.insert(key, val)
        return res
        
