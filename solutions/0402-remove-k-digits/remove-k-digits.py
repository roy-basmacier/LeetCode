# -*- coding:utf-8 -*-


# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
#
#
# Note:
#
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
#
#
#
#
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
#
#
#
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
#
#
#
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
#
#


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # traverse the array
        # keep track of the previous numbers
        # if the previous number is greater than the current number
        # delete the previous number
        if len(num) <= k:
            return '0'
        
        prvNums = [] # Stack
        for ch in num:
            while prvNums != [] and k > 0 and prvNums[-1] > ch:
                prvNums.pop()
                k -= 1
            prvNums.append(ch)
            
        if k > 0:
            prvNums = prvNums[:-k]
        
        # get rid of leading zeros
        res = ''
        i = 0
        while i < len(prvNums) and prvNums[i] == '0':
            i += 1
        
        while i < len(prvNums):
            res += prvNums[i]
            i += 1
            
        if len(res) == 0:
            res = '0'
        return res
        
        
