# -*- coding:utf-8 -*-


# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
#
# 	The same word in the dictionary may be reused multiple times in the segmentation.
# 	You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
#
#
# Example 2:
#
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
#


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
                
        
                                
