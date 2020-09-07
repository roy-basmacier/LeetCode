class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        n = bin(n)[2:]
        foundOne = False
        for ch in n:
            if ch == '1':
                if foundOne:
                    return False
                else:
                    foundOne = True
        return True
        