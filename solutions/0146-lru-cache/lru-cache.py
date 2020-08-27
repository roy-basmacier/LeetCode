# -*- coding:utf-8 -*-


# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
#
#  
#


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
