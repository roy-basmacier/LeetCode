# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode, path: List[str] = []) -> List[str]:
        res = []
        if root == None:
            return res
        
        path.append(str(root.val))
        
        if root.right == None and root.left == None:
            res = ["->".join(path)]

        if root.left != None:
            res += self.binaryTreePaths(root.left, path)
            
        if root.right != None:
            res += self.binaryTreePaths(root.right, path)
        
        path.pop()
        return res