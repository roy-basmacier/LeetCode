class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            if curSum + nums[i] > nums[i]:
                curSum += nums[i]
            else:
                curSum = nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum
            
