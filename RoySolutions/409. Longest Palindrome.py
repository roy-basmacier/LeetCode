class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        
        maxOdd = 0
        longestLen = 0
        for count in freq.values():
            if count % 2 == 0:
                longestLen += count
            else:
                maxOdd = 1
                longestLen +=  count-1
        return longestLen + maxOdd
        