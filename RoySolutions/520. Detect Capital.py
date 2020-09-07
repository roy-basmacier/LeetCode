class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        index = {}
        for i, ch in enumerate(word):
            if ord(ch) <= ord("Z"):
                index[i] = True
        cnt = len(index)
        if cnt == 1:
            return 0 in index
        
        return cnt == 0 or cnt == len(word)
        