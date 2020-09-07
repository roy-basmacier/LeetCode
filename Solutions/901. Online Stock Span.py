class StockSpanner(object):

    def __init__(self):
        self.history = []
        self.span = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if self.history == []:
            self.span.append(1)
        else:
            n = len(self.history)
            i = n - 1
            while i >= 0 and price >= self.history[i]:
                i -= self.span[i]
            self.span.append(n-i)

                    
        
        self.history.append(price)
        return self.span[-1]
        
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)