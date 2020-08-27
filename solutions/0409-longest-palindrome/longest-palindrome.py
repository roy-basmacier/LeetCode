# -*- coding:utf-8 -*-


# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#
#  
# Example 1:
#
#
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
#
# Example 2:
#
#
# Input: s = "a"
# Output: 1
#
#
# Example 3:
#
#
# Input: s = "bb"
# Output: 2
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 2000
# 	s consits of lower-case and/or upper-case English letters only.
#
#


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
        
