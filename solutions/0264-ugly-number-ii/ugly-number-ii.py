# -*- coding:utf-8 -*-


# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
# Note:  
#
#
# 	1 is typically treated as an ugly number.
# 	n does not exceed 1690.
#


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return n
        # if n == 2:
        #     return 2
        # if n == 3:
        #     return 3
        # if n == 4:
        #     return 5
        heap = set()
        heap.add(1)
        while n > 0:
            num = min(heap)
            if num * 2 not in heap:
                heap.add(num * 2)
            if num * 3 not in heap:
                heap.add(num * 3)
            if num * 5 not in heap:
                heap.add(num * 5)

            heap.remove(num)
            n -= 1
        return num
