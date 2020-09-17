class Solution:
        
    def tribonacci(self, n: int) -> int:
        # Time  Complexity -> O(n)
        # Space Complexity -> O(1)
        if n == 0:
            return 0
        if n < 3:
            return 1
        res = 0
        f = 0
        s = 1
        t = 1
        for i in range(n-2):
            res = f + s + t
            f = s
            s = t
            t = res
        return res