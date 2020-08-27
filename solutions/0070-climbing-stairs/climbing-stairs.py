# -*- coding:utf-8 -*-


# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 45
#
#


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1 -> 1
        # 2 -> 2
        # 3 -> 3
        # 4 -> 5 1 1 1 1 / 2 1 1 / 1 2 1 / 1 1 2 / 2 2
        # 5 -> 8
        if n < 3:
            return n
        prv = 1
        nxt = 2
        for i in range(n-2):
            temp = nxt
            nxt += prv
            prv = temp
        return nxt
