class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d = {}
        punc = ',.?!\'\"-:;'
        cnt = 0
        key = None
        for bword in banned:
            d[bword] = -99
            
        for p in punc:
            paragraph = paragraph.replace(p, ' ')
            
        for word in paragraph.split(' '):
            if word.isalpha():
                word = word.lower()
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
                if d[word] > cnt:
                    cnt = d[word]
                    key = word
        return key
        
        