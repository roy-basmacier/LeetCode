# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxLength = 0
        
    def helper(self, node, depth):
        if not node:
            return 0
        if not node.left and not node.right:
            return depth
        leftVal = 0
        rightVal = 0
        if node.left:
            leftVal = self.helper(node.left, 1)
        if node.right:
            rightVal = self.helper(node.right, 1)

        self.maxLength = max(self.maxLength, rightVal + leftVal)

        return max(leftVal, rightVal) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        
        self.helper(root, 0)
        
        return self.maxLength