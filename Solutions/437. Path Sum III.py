# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = 0
    def pathSum(self, root, k):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        
        memo = {0:1}
        
        def pathFinder(node, path=0):
            path += node.val
            
            oldPath = path - k
            
            if oldPath not in memo:
                memo[oldPath] = 0
                
            self.res += memo[oldPath]
            
            if path not in memo:
                memo[path] = 0
                
            memo[path] += 1
            
            
            if node.left:
                pathFinder(node.left, path)
            if node.right:
                pathFinder(node.right, path)
                
            memo[path] -= 1
        

        pathFinder(root)
        
        return self.res
            