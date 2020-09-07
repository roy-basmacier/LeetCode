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
            