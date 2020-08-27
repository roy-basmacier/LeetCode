# -*- coding:utf-8 -*-


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
#
# 	You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# 	After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
#
#
# Example:
#
#
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#


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
