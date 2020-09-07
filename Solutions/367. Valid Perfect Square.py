class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        oddSum = 0
        while oddSum <= num:
            if oddSum == num:
                return True
            oddSum += i
            i += 2
        return False