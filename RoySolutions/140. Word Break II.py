class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # check if the string is splitable
        def isSplitable(s):
            memo = [0 for i in range(len(s) + 1)]
            memo[0] = 1
            for i in range(1, len(s)+1):
                for j in range(i):
                    if memo[j] and s[j:i] in wordDict:
                        memo[i] = 1
            return memo[-1]
        
        if not isSplitable(s):
            return []
        stack = [("", 0)]
        res = []
        while stack:
            sentence, l = stack.pop()
                
            if l == len(s):
                res.append(sentence[1:])
            r = l
            while r < len(s):
                if s[l:r+1] in wordDict:
                    stack.append((sentence + " "+ s[l:r+1], r+1))
                r += 1
        return res
                
        
                                