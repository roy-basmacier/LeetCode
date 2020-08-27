# -*- coding:utf-8 -*-


#
# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
#
#
#
# Example 1:
#
# Input: "()"
# Output: True
#
#
#
# Example 2:
#
# Input: "(*)"
# Output: True
#
#
#
# Example 3:
#
# Input: "(*))"
# Output: True
#
#
#
# Note:
#
# The string size will be in the range [1, 100].
#
#


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # travrerse from left to right
        leftCount = 0
        for ch in s:
            if ch == ")":
                leftCount -= 1
            else:
                leftCount += 1
                
            if leftCount < 0 :
                return False
        
        # check if it is balanced
        if leftCount == 0:
            return True
        
        # traverse from right to left
        rightCount = 0
        for i in range(len(s)-1, -1, -1):
            ch = s[i]
            if ch == "(":
                rightCount -= 1
            else:
                rightCount += 1
                
            if rightCount < 0:
                return False
        return True
