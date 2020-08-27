# -*- coding:utf-8 -*-


# Design an Iterator class, which has:
#
#
# 	A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# 	A function next() that returns the next combination of length combinationLength in lexicographical order.
# 	A function hasNext() that returns True if and only if there exists a next combination.
#
#
#  
#
# Example:
#
#
# CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.
#
# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false
#
#
#  
# Constraints:
#
#
# 	1 <= combinationLength <= characters.length <= 15
# 	There will be at most 10^4 function calls per test.
# 	It's guaranteed that all calls of the function next are valid.
#
#


class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.combinations = []
        self.index = 0
        
        def dfs(s, i, curr):
            if curr == combinationLength:
                self.combinations.append(s)
                return
            for j in range(i, len(characters)):
                dfs(s + characters[j], j+1, curr+1)
        
        dfs('', 0, 0)
        print(self.combinations)

    def next(self):
        """
        :rtype: str
        """
        self.index += 1
        return self.combinations[self.index-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.combinations)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
