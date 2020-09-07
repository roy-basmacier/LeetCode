class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        p = 1
        while n:
            if n & 1:
                p *= x
            x *= x
            n >>= 1
        return p
        