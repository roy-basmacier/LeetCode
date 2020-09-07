class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # travrerse from left to right
        leftCount = 0
        for ch in s:
            if ch == ")":
                leftCount -= 1
            else:
                leftCount += 1
                
            if leftCount < 0 :
                return False
        
        # check if it is balanced
        if leftCount == 0:
            return True
        
        # traverse from right to left
        rightCount = 0
        for i in range(len(s)-1, -1, -1):
            ch = s[i]
            if ch == "(":
                rightCount -= 1
            else:
                rightCount += 1
                
            if rightCount < 0:
                return False
        return True