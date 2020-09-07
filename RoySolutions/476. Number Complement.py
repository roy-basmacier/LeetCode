class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = 2
        while n <= num:
            n *= 2
        return n - num - 1
        