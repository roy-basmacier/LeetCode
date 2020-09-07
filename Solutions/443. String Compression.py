class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars) - 1:
            if chars[i] == chars[i+1]:
                j = i+1

                while j < len(chars) and chars[i] == chars[j]:
                    j += 1

                for k in range(len(str(j-i))):
                    chars[i+k+1] = str(j-i)[k]
                    
                for k in range(j-i - len(str(j-i))-1):
                    chars.pop(1+i+len(str(j-i)))
                i += len(str(j-i))
            i += 1
        return len(chars)
            