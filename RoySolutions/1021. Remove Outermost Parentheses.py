class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = 0
        res = ''
        for i in range(1, len(S)):
            if S[i] == '(':
                count += 1
            if count != 0:            
                res += S[i]
            if S[i] == ')':
                count -= 1
            
            
            print(S[i], count)

            
            
                
        return res