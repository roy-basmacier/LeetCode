class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomFreq = {}
        magazineFreq = {}
        for ch in ransomNote:
            if ch not in ransomFreq:
                ransomFreq[ch] = 0
            ransomFreq[ch] += 1
        
        for ch in magazine:
            if ch not in magazineFreq:
                magazineFreq[ch] = 0
            magazineFreq[ch] += 1
        
        for ch in ransomNote:
            if ch not in magazineFreq:
                return False
            if magazineFreq[ch] < ransomFreq[ch]:
                return False
        return True