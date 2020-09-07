class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        leftProduct = 1
        output = []
        for i in range(len(nums)):
            output.append(leftProduct)
            leftProduct *= nums[i]
        
        rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= rightProduct
            rightProduct *= nums[i]
        return output