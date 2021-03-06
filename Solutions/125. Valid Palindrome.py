class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time  Complexity -> O(n)
        # Space Complexity -> O(1)

        l = 0 
        r = len(s)-1
        s = s.lower()
        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1
                
            if l >= r:
                break
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
            
            
        return True