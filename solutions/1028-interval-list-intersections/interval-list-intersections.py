# -*- coding:utf-8 -*-


# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
#
#
#  
#
# Example 1:
#
#
#
#
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
#
#  
#
# Note:
#
#
# 	0 <= A.length < 1000
# 	0 <= B.length < 1000
# 	0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
#
#
#


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        a = 0
        b = 0
        output = []
        while a < len(A) and  b < len(B):
            aStart = A[a][0]
            aEnd = A[a][1]
            bStart = B[b][0]
            bEnd = B[b][1]
            
            outStart = max(aStart, bStart)
            outEnd = min(aEnd, bEnd)
            if outStart <= outEnd:
                output.append((outStart, outEnd))
                
            if aEnd > bEnd:
                b += 1
            else:
                a += 1
        return output
