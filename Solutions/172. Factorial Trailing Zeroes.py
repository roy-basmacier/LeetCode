class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        num = 5
        while n >= num:
            count += n / num
            num *= 5
        return count
        