
# Definition for a Node.
class Node(object)
    def __init__(self, val, prev, next, child)
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object)
    def flatten(self, head)
        
        type head Node
        rtype Node
        
        if not head
            return None
        queue = [head]
        stack = [] # keeps parent's next
        while queue != []
            node = queue[0]
            queue = queue[1]
               
            if node.child
                
                stack.append(node.next)
                node.next = node.child
                node.next.prev = node
                node.child = None

            if not node.next and len(stack)  0
                afterMergeNode = stack.pop()
                node.next = afterMergeNode
                if afterMergeNode
                    afterMergeNode.prev = node
            if node.next   
                queue.append(node.next)
        return head

                
                
        
        