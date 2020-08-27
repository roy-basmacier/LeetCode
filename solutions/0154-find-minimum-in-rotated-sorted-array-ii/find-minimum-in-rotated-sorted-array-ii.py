# -*- coding:utf-8 -*-


# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# The array may contain duplicates.
#
# Example 1:
#
#
# Input: [1,3,5]
# Output: 1
#
# Example 2:
#
#
# Input: [2,2,2,0,1]
# Output: 0
#
# Note:
#
#
# 	This is a follow up problem to Find Minimum in Rotated Sorted Array.
# 	Would allow duplicates affect the run-time complexity? How and why?
#
#


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 7,1,2,3,4,5,6
        # if left > middle -> pivot is on the left side
        # 7, 8, 9, 1, 2, 6
        # if right < middle -> pivot is on the right side
        # duplicates -> if middle == right then move right by one
        
        left = 0
        right = len(nums)-1
        while left < right:
            middle = (left + right)/2
            
            if nums[left] > nums[middle]:
                right = middle
                
            elif nums[right] < nums[middle]:
                left = middle+1
            else:
                right -=1
                
        return nums[left]
