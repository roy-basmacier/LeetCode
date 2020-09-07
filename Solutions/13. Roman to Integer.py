class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        i = 0
        while i < len(s):
            if i != len(s) - 1:
                if d[s[i]] >= d[s[i+1]]:
                    res += d[s[i]]
                else:
                    res += d[s[i+1]]-d[s[i]]
                    i += 1
            else:
                res += d[s[i]]
            i += 1
        return res
        