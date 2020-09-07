class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = bin(n)[2:].zfill(32)[::-1]
        return int(x, 2)