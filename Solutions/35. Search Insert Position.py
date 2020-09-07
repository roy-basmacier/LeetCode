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
            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        if target > nums[left]:
            return left + 1
        return left