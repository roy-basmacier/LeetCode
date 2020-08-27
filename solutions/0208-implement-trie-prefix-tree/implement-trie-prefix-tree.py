# -*- coding:utf-8 -*-


# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
#
#
# Note:
#
#
# 	You may assume that all inputs are consist of lowercase letters a-z.
# 	All inputs are guaranteed to be non-empty strings.
#
#


class Node():    
    def __init__(self, ch):
        self.letter = ch
        self.children = []

class Trie(object):
   
        
        
    def __init__(self):
        """
        Initialize your data structure here.
        """ 
        self.root = Node(' ')
        

    def insert(self, word):
        print("-------------inserting:", word)
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        i = 0
        n = len(word)
        curr = self.root   
        while i < n:
            found = False
            for child in curr.children:
                if str(child.letter) == word[i]:
                    found = True
                    curr = child
                    break
            if not found:
                curr.children.append(Node(word[i]))
                curr = curr.children[-1]
            i += 1
        curr.children.append(Node('$'))
                
        
                
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        print("-------------searching:", word)

        if not self.root:
            return False
        
        i = 0
        n = len(word)
        curr = self.root
        while i < n:
            found = False
            for child in curr.children:
                if str(child.letter) == word[i]:
                    found = True
                    curr = child
                    i += 1
                    break
            if not found:
                return False
        
        for child in curr.children:
            if str(child.letter) == '$':
                return True
        return False
                
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not self.root:
            return False
        
        i = 0
        n = len(prefix)
        curr = self.root
        while i < n:
            found = False
            for child in curr.children:
                if str(child.letter) == prefix[i]:
                    found = True
                    curr = child
                    i += 1
                    break
            if not found:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
