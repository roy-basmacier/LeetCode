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
        