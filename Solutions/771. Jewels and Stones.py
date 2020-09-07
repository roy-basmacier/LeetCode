class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set()
        for ch in J:
            if ch not in jewels:
                jewels.add(ch)
        count = 0
        for ch in S:
            if ch in jewels:
                count += 1
        return count