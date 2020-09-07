class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        i = 1
        j = -1
        _x = x
        while _x > 0:
            _x //= 10
            j += 1
        half = (j + 1) //2
        while i <= half and x > 0:
            print(x % 10,(x // (10**j)) % 10)
            if x % 10 != (x // (10**j)) % 10:
                return False
            i += 1
            j -= 2
            x//= 10
            
            
        return True