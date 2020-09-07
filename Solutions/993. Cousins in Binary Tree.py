# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def dfs(node, depth):
            if node.right:
                if node.right.val == y or node.right.val == x:
                    parent[node.right.val] = depth , node.val
                dfs(node.right, depth + 1)
            if node.left:
                if node.left.val == y or node.left.val == x:
                    parent[node.left.val] = depth , node.val
                dfs(node.left, depth + 1)
                
        parent = {}
        dfs(root, 0)
        _x, _y = parent.get(x, (-1, -1)), parent.get(y,(-2,-2))
        return _x[0] == _y[0] and _x[1] != _y[1]
        