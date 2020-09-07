class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:      
        words.sort(key=len, reverse=True)
        S = ''
        for i in range(len(words)):
            found = False
            if words[i] + '#' in S:
                found = True
            if not found:
                S += words[i] + '#'
        return len(S)
            
                
        