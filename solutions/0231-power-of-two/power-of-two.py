# -*- coding:utf-8 -*-


# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
#
# Input: 1
# Output: true 
# Explanation: 20 = 1
#
#
# Example 2:
#
#
# Input: 16
# Output: true
# Explanation: 24 = 16
#
# Example 3:
#
#
# Input: 218
# Output: false
#


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        n = bin(n)[2:]
        foundOne = False
        for ch in n:
            if ch == '1':
                if foundOne:
                    return False
                else:
                    foundOne = True
        return True
        
