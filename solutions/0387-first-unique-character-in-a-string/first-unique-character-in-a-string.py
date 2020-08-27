# -*- coding:utf-8 -*-


# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Examples:
#
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.
#
#
#  
#
# Note: You may assume the string contains only lowercase English letters.
#


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
        
        
