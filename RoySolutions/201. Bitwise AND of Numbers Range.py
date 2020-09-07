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