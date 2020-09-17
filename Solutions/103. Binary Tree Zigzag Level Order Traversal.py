# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Time  Complexity -> O(n)
        # Space Complexity -> O(n)
        if not root:
            return []
        queue = [(root, 0)]
        res = []
        while queue:
            node, d = queue[0]
            queue = queue[1:]
            if len(res) <= d:
                res.append([])
            res[d].append(node.val)
            
            # add to queue from right to left
            if node.right:
                queue.append((node.right,d+1))
            if node.left:
                queue.append((node.left,d+1))
            
        for i in range(len(res)):
            if i % 2 == 0:
                res[i] = res[i][::-1]
        return res
                
            
            