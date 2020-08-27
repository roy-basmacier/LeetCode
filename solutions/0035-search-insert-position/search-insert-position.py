# -*- coding:utf-8 -*-


# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
#
# Input: [1,3,5,6], 5
# Output: 2
#
#
# Example 2:
#
#
# Input: [1,3,5,6], 2
# Output: 1
#
#
# Example 3:
#
#
# Input: [1,3,5,6], 7
# Output: 4
#
#
# Example 4:
#
#
# Input: [1,3,5,6], 0
# Output: 0
#
#


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search
        left = 0 
        right = len(nums)-1
        
        while left < right:
            middle = (right + left) // 2
            print(left, middle, right)
            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        if target > nums[left]:
            return left + 1
        return left
