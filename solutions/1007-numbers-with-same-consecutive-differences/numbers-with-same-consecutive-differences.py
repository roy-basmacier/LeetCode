# -*- coding:utf-8 -*-


# Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.
#
# Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.
#
# You may return the answer in any order.
#
#  
#
# Example 1:
#
#
# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
#
#
#
# Example 2:
#
#
# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
#
#  
#
#
# Note:
#
#
# 	1 <= N <= 9
# 	0 <= K <= 9
#
#


class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        
        memo = {}
        # populate memo
        for i in range(0, 10):
            # check i + k and i - k
            key = str(i)
            memo[key] = []
            
            if i + K < 10:
                # find number
                memo[key].append(str(i+K))
                
            if abs(i - K) < 10 and  abs(i-K) == i - K:
                # find number
                memo[key].append(str(abs(i-K)))
            
                
        res = set()
        stack = [str(i) for i in range(1,10)]
        if N == 1:
            stack.append("0")
        while stack:
            s = stack.pop()
            if len(s) == N:
                res.add(s)
            else:
                
                for nextCh in memo[s[-1]]:
                    stack.append(s+nextCh)
        return res
            
            
            
            
        
        
