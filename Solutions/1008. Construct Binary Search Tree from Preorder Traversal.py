# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        self.index = 0
        def helper(bound):
            if self.index >= len(preorder) or preorder[self.index] > bound:
                return None
            
            node = TreeNode(preorder[self.index])
            self.index += 1
            node.left = helper(node.val)
            node.right = helper(bound)
            return node
        
        return helper(float('inf'))
            
            