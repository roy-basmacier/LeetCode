class Solution:
    def myAtoi(self, str: str) -> int:
        def int32(x):
            if x < -2147483648:
                return -2147483648
            if x > 2147483647:
                return 2147483647
            return x
        res = ""
        for ch in str:
            print(ord(ch), ch)
            if (48 <= ord(ch) and ord(ch) <= 57):
                res += ch
            elif ord(ch) == 45 or ord(ch) == 43:
                if res == "":
                    res += ch
                else:
                    break
            elif ord(ch) == 32:
                if res != "":
                    break
            else:
                break
            print(res)
        if res == "" or res == "-" or res == "+":
            return 0
        return int32(int(res))