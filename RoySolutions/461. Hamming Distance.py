class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # n = x^y
        # hamDist = 0
        # while n > 0:
        #     hamDist += (n & 1)
        #     n >>= 1
        # return hamDist
        return bin(x^y).count('1')
        