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