class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s) -1
        res = 0
        for ch in s:
            num = ord(ch) - ord("A") + 1
            res += (26**n * num)
            n -= 1
        return res
            
        
        