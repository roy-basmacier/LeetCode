class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myNumber = 0
        for num in nums:
            myNumber ^= num
        return myNumber