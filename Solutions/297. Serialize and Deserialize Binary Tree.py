# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        queue = [root]
        s = []  
        while queue != []:
            node = queue[0]
            queue.remove(node)
            if not node:
                s.append('null')
            else:
                s.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        while s[-1] == 'null':
            s.pop()
        return '[' + ','.join(s) + ']'
        
            
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        data = data[1:-1] # splice the brackets
        stack = data.split(',')[::-1]
        if len(stack) < 1:
            return TreeNode(data)
        
        root = TreeNode(stack.pop())
        queue = [root]

        while queue != []:
            node = queue[0]
            queue.remove(node)
            if stack != []:
                node.left = TreeNode(stack.pop())
                queue.append(node.left)
            else:
                node.left = None
            if stack != []:
                node.right = TreeNode(stack.pop())
                queue.append(node.right)
            else:
                node.right = None
        return root
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))