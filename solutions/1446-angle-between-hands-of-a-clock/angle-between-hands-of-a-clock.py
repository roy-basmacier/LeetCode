# -*- coding:utf-8 -*-


# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
#
#  
# Example 1:
#
#
#
#
# Input: hour = 12, minutes = 30
# Output: 165
#
#
# Example 2:
#
#
#
#
# Input: hour = 3, minutes = 30
# Output: 75
#
#
# Example 3:
#
#
#
#
# Input: hour = 3, minutes = 15
# Output: 7.5
#
#
# Example 4:
#
#
# Input: hour = 4, minutes = 50
# Output: 155
#
#
# Example 5:
#
#
# Input: hour = 12, minutes = 0
# Output: 0
#
#
#  
# Constraints:
#
#
# 	1 <= hour <= 12
# 	0 <= minutes <= 59
# 	Answers within 10^-5 of the actual value will be accepted as correct.
#
#


class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        # convert the minutes and hours to radian
        # M = m * 6 % 360
        # H = h * 5 * 6 % 360 + M
        # Answer = max(H,M) - min(H, M)
        
        M = (minutes * 6.0) %360
        H = ((hour * 30.0) % 360)  + minutes/2.0
        upper = max(H,M) - min(H,M)
        if upper > 180:
            return 360 - upper
        return upper
