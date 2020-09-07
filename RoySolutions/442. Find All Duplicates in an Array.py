class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # since the array consists of n-1 numbers
        # we can use the index of the array to indicate if we have seen that number
        # check if nums[nums[i]] is positive if it is set it to negative
        # if it is negative we have found a duplicate
        duplicates = []
        # [4,3,2,7,8,2,3,1]
        # [4,-3,-2,-7,8,2,-3,-1]

        for i in range(len(nums)):
            num = abs(nums[i])-1
            if nums[num] < 0:
                duplicates.append(num+1)
            else:
                nums[num] = -nums[num]
        return duplicates
        
        
        