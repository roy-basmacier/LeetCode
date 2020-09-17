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
        # Time  Complexity -> O(n)
        # Space Complexity -> O(n)

        if not root.left and not root.right:
            return root.val
        def helper(node):
            if not node:
                return [float('-inf')] * 2
            
            leftSum = helper(node.left)
            rightSum = helper(node.right)
            
            return [node.val + max(leftSum[0], rightSum[0], 0), max(leftSum + rightSum + [node.val + leftSum[0] + rightSum[0]])]
        return max(helper(root))

        