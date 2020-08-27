# -*- coding:utf-8 -*-


# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Follow up: Do not use any built-in library function such as sqrt.
#
#  
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false
#
#  
# Constraints:
#
#
# 	1 <= num <= 2^31 - 1
#
#


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        oddSum = 0
        while oddSum <= num:
            if oddSum == num:
                return True
            oddSum += i
            i += 2
        return False
