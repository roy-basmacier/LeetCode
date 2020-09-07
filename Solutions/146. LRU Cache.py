class Node:
    def __init__(self, _key, _value):
        self.key = _key
        self.value = _value
        self.prv = None
        self.nxt = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.nxt = self.tail
        self.tail.prv = self.head
    
    def remove(self, node):
        p = node.prv
        n = node.nxt
        p.nxt = n
        n.prv = p
        
        
    def add(self, node):
        p = self.tail.prv
        p.nxt = node
        self.tail.prv = node
        node.prv = p
        node.nxt = self.tail
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.add(node)
        return node.value
        
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            self.remove(self.map[key])
            
        node = Node(key, value)
        self.add(node)
        self.map[key] = node
        if len(self.map) > self.capacity:
            n = self.head.nxt
            self.remove(n)
            del self.map[n.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)