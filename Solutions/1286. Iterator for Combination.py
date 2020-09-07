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