# -*- coding:utf-8 -*-


# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
#  
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#  
# Constraints:
#
#
# 	You may assume that both strings contain only lowercase letters.
#
#


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
