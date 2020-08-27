# -*- coding:utf-8 -*-


# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 
#
#
# Example 1:
#
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#
#
#
# Example 2:
#
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
#
#
# Note:
# The length of the given binary array will not exceed 50,000.
#


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxLength = 0
        d = {0: 0}
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
                
            if count not in d:
                d[count] = i + 1
            else:
                maxLength = max(maxLength, i+1-d[count])
        return maxLength
        
