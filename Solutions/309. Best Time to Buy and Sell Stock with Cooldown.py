class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # 3 states
        # 1) BUY   -> the state for max profit when I can buy        ==> max(BUY, STOCK)
        # 2) STOCK -> the state for max profit when I have a stock   ==> max(STOCK, BUY - price[i])
        # 3) WAIT  -> the state for max profit when I am on cooldown ==> STOCK + PRICE[i]
        
        
        buy = 0
        stock = wait = float('-inf')
        for price in prices:
            stock, buy, wait = max(stock, buy-price), max(buy, wait), stock+price
        return max(buy, wait)