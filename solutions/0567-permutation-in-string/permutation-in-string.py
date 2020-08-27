# -*- coding:utf-8 -*-


# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
#
#  
#
# Example 1:
#
#
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
#
#
# Example 2:
#
#
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#
#
#  
# Constraints:
#
#
# 	The input strings only contain lower case letters.
# 	The length of both given strings is in range [1, 10,000].
#
#


class Solution(object):
    
    def compare(self, arr1, arr2):
        for i in range(26):
            if arr1[i] != arr2[i]:
                return False
        return True
            
    
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        freq = [0 for i in range(26)]
        window = [0 for i in range(26)]
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
            
        
        for i in range(len(s2)-len(s1)):
            if self.compare(freq, window):
                return True
            window[ord(s2[i + len(s1)]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] -= 1
            
            

        return self.compare(freq, window)
                
            
            
            
            
            
        
        
