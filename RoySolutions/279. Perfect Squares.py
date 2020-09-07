class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        count = 0
        perfect_square = n**0.5
        
        if perfect_square.is_integer():
            return 1
        perfect_square = int(perfect_square)
        
        checking = {n}
        while checking:
            count += 1
            new_set = set()
            for i in checking:
                for j in range(1, perfect_square + 1):
                    if i == j**2:
                        return count
                    if i < j**2:
                        break
                    new_set.add(i-j**2)
            checking = new_set
        return count
                       