class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carryOn = 0
        for i in range(len(digits)-1, -1, -1):
            carryOn = 0
            if digits[i] == 9:
                carryOn = 1
            digits[i] += 1
            digits[i] %= 10
            if carryOn == 0:
                break
        if carryOn == 1:
            digits = [1] + digits
        return digits
            
                
        