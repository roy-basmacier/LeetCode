class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        n = len(s)
        freq = {}
        for i, ch in enumerate(s):
            if ch not in freq:
                freq[ch] = i
            else:
                freq[ch] = n
        index = min(freq.values())
        if index == n:
            return -1
        return index
        
        