# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.min_x = 0
        self.layers = {} # x-coord -> [(val, y_pos)]                

        
    def helper(self, node, x, y):
            self.min_x = min(self.min_x, x)
            if node.left:
                self.helper(node.left, x-1, y-1)
                
            if x not in self.layers:
                self.layers[x] = []
                
            self.layers[x].append((node.val, y))
            
            if node.right:
                self.helper(node.right, x+1, y-1)
                
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
                
        self.helper(root, 0, 0)
        n = len(self.layers)
        res = [[] for _ in range(n)]
        
        for x, nodes in self.layers.items():
            idx = x - self.min_x
            nodes.sort(key=lambda x: (-x[1], x[0]))
            # print(nodes)
            for val, y in nodes:
                res[idx].append(val)
            
            
            
        return res
        