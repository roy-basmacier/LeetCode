# -*- coding:utf-8 -*-


# Given two strings text1 and text2, return the length of their longest common subsequence.
#
# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
#
#  
#
# If there is no common subsequence, return 0.
#
#  
# Example 1:
#
#
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
#
# Example 2:
#
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
#
# Example 3:
#
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
#  
# Constraints:
#
#
# 	1 <= text1.length <= 1000
# 	1 <= text2.length <= 1000
# 	The input strings consist of lowercase English characters only.
#
#


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        # dynamic programming
        # bottom right to top left (bottom up approach)
        # if they are the same characters then cell = diagonal cell + 1
        # else it is the max of upper or lower cell

        dp = [[None for _ in range(n+1)] for _ in range(m+1)]
        
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            
            if text1[i] == text2[j]:
                if dp[i-1][j-1] == None:
                    dp[i-1][j-1] = helper(i-1, j-1)
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                if dp[i-1][j] == None:
                    dp[i-1][j] = helper(i-1, j)
                if dp[i][j-1] == None:
                    dp[i][j-1] = helper(i, j-1)
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            return dp[i][j]
        helper(m-1, n-1)
        return dp[m-1][n-1]
