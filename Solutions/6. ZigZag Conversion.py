class Solution:
    def convert(self, s: str, row: int) -> str:
        if row < 2:
            return s
        res = ''
        #first row
        k = 0
        index = (2 * row - 2) * k
        while index < len(s):
            res += s[index]
            k += 1
            index = (2 * row - 2) * k
          
        print('f', res)    
        # the rows in between first and last rows
        for i in range(1, row-1):
            k = 0
            index = (2 * row - 2) * k + i
            while index < len(s):
                res += s[index]
                index = (2 * row - 2) * (k+1) -i
                if index < len(s):
                    res += s[index]
                else:
                    break
                k += 1
                index = (2 * row - 2) * k + i
        print('b', res)
        #last row
        k = 0
        index = (2 * row - 2) * k + row -1
        while index < len(s):
            res += s[index]
            k += 1
            index = (2 * row - 2) * k + row -1
        print('l', res)
        return res