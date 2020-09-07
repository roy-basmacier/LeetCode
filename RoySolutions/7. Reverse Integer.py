class Solution:
    def reverse(self, x: int) -> int:
        def overflow(x):
            if x<-2147483648 or x > 2147483647:
                return 0
            else:
                return x
        if x < 0:
            x = str(x)[1::]
            return overflow(-1 * int(x[::-1]))
        return overflow(int(str(x)[::-1]))
            