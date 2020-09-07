# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper (node:TreeNode, maxval):
            if node:
                r = helper(node.right, maxval)
                if r > maxval:
                    maxval = r
                node.val += maxval
                if node.val > maxval:
                    maxval = node.val
                l = helper(node.left, maxval)
                if l > maxval:
                    maxval = l
                return maxval
            else:
                return 0

        helper(root, 0)
        return root
    
    
        #sum of our parent plus right side