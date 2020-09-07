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