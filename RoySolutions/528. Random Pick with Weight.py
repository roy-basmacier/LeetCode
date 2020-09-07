class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.interval = 10000
        self.map = [] # maps index to end interval for over all interval
        total = sum(w)
        currEnd = 0
        for i in range(len(w)):
            currEnd = currEnd + (self.interval * w[i]) // total
            self.map.append(currEnd)
        print(self.map)
        print(w)
        
    def pickIndex(self):
        """
        :rtype: int
        """
        randSelection = random.randint(1, self.interval)
        
        for i, end in enumerate(self.map):
            if randSelection <= end:
                return i
        print(randSelection)
        return len(self.map) - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()