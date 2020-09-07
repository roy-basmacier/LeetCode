# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root:
            
            if root.left != None and root.left.left == None and root.left.right == None:
                return root.left.val + self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
            
            return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
        else:
            return 0
        