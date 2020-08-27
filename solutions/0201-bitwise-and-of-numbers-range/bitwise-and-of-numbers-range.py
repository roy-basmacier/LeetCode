# -*- coding:utf-8 -*-


# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
#
# Example 1:
#
#
# Input: [5,7]
# Output: 4
#
#
# Example 2:
#
#
# Input: [0,1]
# Output: 0


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            n >>= 1
            m >>= 1
            i += 1
            
        n <<= i
        return n
